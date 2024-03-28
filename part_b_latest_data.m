% Define ThingSpeak channel ID and read API key
channel_id = 2488446;
read_api_key = 'BEQ2ZGBOU739MUN5';

% Function to read the latest data from ThingSpeak
function latest_data = readLatestData(channel_id, read_api_key)
    data = thingSpeakRead(channel_id, 'ReadKey', read_api_key, 'Fields', [1,2,3], 'NumPoints', 1);
    latest_data.temperature = data(1, 1);
    latest_data.humidity = data(1, 2);
    latest_data.co2 = data(1, 3);
end

% Function to display the latest sensor data
function displayLatestData(data)
    fprintf('Latest Sensor Data:\n');
    fprintf('Temperature sensor data: %.2f°C\n', data.temperature);
    fprintf('Humidity sensor data: %.2f%%\n', data.humidity);
    fprintf('CO2 sensor data: %.2f ppm\n', data.co2);
end

% Reading latest data from ThingSpeak
latest_data = readLatestData(channel_id, read_api_key);

% Displaying latest sensor data
displayLatestData(latest_data);
