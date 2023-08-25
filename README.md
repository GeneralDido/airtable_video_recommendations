
# Airtable Video Recommendations

  

The Airtable Video Recommendations app collects YouTube channel stats, identifies best-performing videos, and uses OpenAI to generate video title recommendations based on the best-performing titles.

  

## Table of Contents

- [Setup](#setup)

- [Dependencies](#dependencies)

- [Modules Overview](#modules-overview)

- [best_performing_videos.py](#best_performing_videospy)

- [recommendations.py](#recommendationspy)

- [yt_channel_stats.py](#yt_channel_statspy)

- [main.py](#mainpy)

- [Execution](#execution)
  

## Setup

  

1. Clone the repository.

2. Set up environment variables in a `.env` file in the root directory. See .env.example for more information.

3. Install the necessary packages using `pip install -r requirements.txt`.

  

## Dependencies

  

-  `google_api_python_client`: Google API client library.

-  `isodate`: Date-time utilities.

-  `openai`: OpenAI GPT-3 API client library.

-  `pyairtable`: Airtable Python client.

-  `python-dotenv`: Python dotenv library.

  

## Modules Overview

  

### -best_performing_videos.py

  

Identifies and stores the best-performing videos from a given YouTube channel into Airtable.

  

#### Class `BestPerformingVideos`:

  

-  `generate()`: Collects the best-performing videos for all channels in the Airtable and updates the respective records.

  

### -recommendations.py

  

Generates video title recommendations using OpenAI based on the best-performing titles.

  

#### Class `Recommendations`:

  

-  `generate()`: Retrieves the best-performing video titles from Airtable and uses OpenAI to generate new video title recommendations.

  

### -yt_channel_stats.py

  

Collects and updates YouTube channel stats in Airtable.

  

#### Class `YTChannelStats`:

  

-  `generate()`: Collects statistics for YouTube channels listed in the Airtable and updates the respective records.

  

### -main.py

  

Main execution script which combines the functionalities of other modules to provide the complete workflow.

  

## Execution

  

1. Execute `main.py` to start the process.

2. The script will update YouTube channel stats in the Airtable, identify best-performing videos, and generate new video title recommendations.

  

## License

  

[MIT License](https://opensource.org/licenses/MIT)