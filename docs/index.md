# Temperature and Humidity Unit
## Assembly
![Pico Temperature and Humidity Unit](/docs/images/pico-temp-humidity-unit.jpg)

### Components:
    * Raspberry Pi Pico
    * DHT11
    * HC-05 Bluetooth Module
    * 10k Ohm Resistor
    * 8x Jumper Wire


## Setup
The next step after assembling the circuit is to put the code ([dht11TempHumidity.py](/temperature-humidity-unit/dht11TempHumidity.py)) onto Raspberry Pi Pico.
1. Press the BOOTSEL button and hold it while you connect the other end of the micro USB cable to your Raspberry Pi 4.
2. Run Thonny IDE.
3. The current version of Python used is displayed in the bottom right corner of Thonny window.
4. Click on the Python version and choose "MicroPython (Raspberry Pi Pico)".
5. Click the Install button in the popup dialog to copy the MicroPython firmware to Raspberry Pi Pico.
6. Open dht11TempHumidity.py file in Thonny.
7. Save this file as main.py and select Raspberry Pi Pico as the target device.

Pico will now automatically run the code in main.py file when powered.

After disconnecting the Pico from power and reconnecting it again you should notice the onboard LED being on for a few seconds and then blinking at regular intervals. \
![Pico blinking LED](/docs/images/pico-temp-humidity-blinking-led.gif) \
This means the Python program is running and temperature and humidity data is being sent to the HC-05 transceiver.

# Raspberry Pi


## Dependencies
```bat
sudo apt-get install bluetooth
sudo apt-get install libbluetooth-dev
pip install PyBluez
pip install paho-mqtt
```

## Pairing with HC05 Bluetooth module
Run bluetoothctl:
```bat
sudo bluetoothctl
```
Scan for other devices:
```bat
bluetoothctl scan on
```
Note the MAC address of the Bluetooth module and pair and connect devices:
```bat
bluetoothctl pair MAC_ADDRESS
```
bluetoothctl will promp for the PIN code. By default it is 1234.
```bat
bluetoothctl connect MAC_ADDRESS
```
Paired Bluetooth devices can be check with:
```bat
bluetoothctl paired-devices
```

# HiveMQ
This section will explain how to create free HiveMQ cluster. \
https://www.hivemq.com/

# InfluxDB
This section will explain how to create and setup free InfluxDB database. \
https://cloud2.influxdata.com/signup

## Creating a bucket
https://docs.influxdata.com/influxdb/cloud/organizations/buckets/create-bucket/

First of all we need to create a bucket to store our time series data. Navigate to **Load Data** menu and go to **Buckets**. Then click the **Create Bucket** button.

![Create a bucket](/docs/images/influxdb-create-bucket.jpg)

Enter a name for the bucket, in this case we have chosen **apartment-env-data**. Optionally set a retention period for the data stored in the bucket. For example, specify to delete the data older than 7 days. Click **Create** to finish.

![Create a bucket](/docs/images/influxdb-create-bucket-dialog.jpg)


## MQTT Subscribtion

InfluxDb allows to use its native MQTT connection to subscribe to a MQTT broker and store the data in the real time database.

*Unfortunately, Native MQTT is not available in the free tier of InfluxDb. To unlock access to MQTT subscriber, you need to upgrade to a paid plan. In this example, Usage-Based Plan is used.*

To subscribe to the MQTT Broker of your choice.navigate to **Native Subscriptions** and click **Create Subscription**.

![Create a bucket](/docs/images/influxdb-create-subscription.jpg)

Time to set the **Broker Details**. Set the **Subscription Name** to any of your choice, *env-sensor* is used in this project.

Copy the Hostname and Port of your MQTT Broker into the fields. If it is a public broker, leave the **Enable SSL** off.

In this project, we are using HiveMQ cloud cluster, which allows secure connections only. In such case, **Enable SSL** must be toggled on as the connection is authenticated using username and password credentials.

Set the **Security Details** to **Basic** and enter your HiveMQ Broker access credentials.

![Create a bucket](/docs/images/influxdb-create-mqtt-details.jpg)

In the **Subscribe to topic** section, enter your MQTT topic name, to which the data is being published from a client deployed on Raspberry Pi. In this project it is *sensor-temp-humidity*.

After that, select the storage bucket which we have created earlier - *apartment-env-data*.

![Create a bucket](/docs/images/influxdb-create-mqtt-topic.jpg)

In the next section we are specifying the **Data format** incoming from the MQTT broker. In this case the data is sent as **JSON**.

InfluxDb can automatically set a **Timestamp** to incoming data, but since our MQTT message already contains a timestamp, we will use it instead.

Set the **JSON Path to Timestamp** to *$.timestamp* as it is in the MQTT message payload and **Timestamp precision** to *seconds*.

![Create a bucket](/docs/images/influxdb-create-mqtt-dataformat.jpg)

**Measurement** in InfluxDB describes the data stored in the associated fields. This can be set from a field in JSON, if our message would contain a *type* field for example to describe the data measured, or it can be set explicitly in InfluxDb. In this project, the JSON data does not have such a field and we will name the incoming data as *environment*.

In the next section we will specify **Tags** and **Fields**. Tags and Fields in InfluxDb are key-value pairs that record metadata (data names) and data values. The difference is that Tags are optional and are indexed, which makes the queries on data quicker.

We will set a **Tag** to be the *deviceId* coming from the JSON content at *\$.deviceId* and set its type to *String*.

After that we add two **Fields**. The first one being the *temperature* with the JSON path set to *\$.temperature* and the second field named *humidity* with the path *\$.humidity*. Both these fields are set as *Float* data type.

![Create a bucket](/docs/images/influxdb-create-mqtt-fields-tags.jpg)

With these details specified, we can now **Save subscription** to create a connection to the MQTT Broker.

After that, you should see the *env-sensor* subscription in the **Native Subscriptions** section with the status *RUNNING*.

![Create a bucket](/docs/images/influxdb-create-mqtt-created.jpg)

From the side menu, navigate to **Data Explorer**. In this section we can create a simple query to the database and plot the data on a simple graph.

**From** the bucket *apartment-env-data* select **Measurement** *environment* and **filter** by our *deviceId* tag specified earlier and *humidity*, *temperature* fields. Click **Submit** button to send the query and plot the data on a Band graph.

You should now see the data incoming from the Raspberry Pi, through the MQTT Broker and into the InfluxDb real time database.

![Create a bucket](/docs/images/influxdb-data-explorer.jpg)

