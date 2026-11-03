# ApplyBot

ApplyBot is a Discord bot designed to streamline the application process within your server. It provides an interactive panel where users can click to start an application, which is then conducted through direct messages. The bot handles the entire application process, from collecting responses to notifying users and sending the final application to a specified channel. It includes features for canceling applications and providing feedback to applicants.

## Install

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ApplyBot.git
   cd ApplyBot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Discord bot token and the application channel ID:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   APPLICATION_CHANNEL_ID=your_application_channel_id
   ```

## Use

1. Start the bot:
   ```bash
   python bot.py
   ```

2. In your Discord server, use the command `!applypanel` to create an application panel.

3. Users can click the "Bewerben" button to start the application process. They will receive a direct message with the first question.

4. Users can answer the questions in the direct message. If they want to cancel the application, they can use the `!cancel` command.

5. Once all questions are answered, the bot will send the application to the specified channel and notify the user.

---

More Discord bot projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/1adf7c6c-af3c-438f-9b19-17dd35085b40?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=1adf7c6c-af3c-438f-9b19-17dd35085b40
