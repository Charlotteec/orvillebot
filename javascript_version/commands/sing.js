const { SlashCommandBuilder } = require('discord.js');

var fs = require('fs');

try {
    var data = fs.readFileSync('assets/deadofnight.txt', 'utf8');
    var lyrics = (data.toString());
} catch(e) {
    console.log('Error:', e.stack);
}


module.exports = {
	data: new SlashCommandBuilder()
		.setName('sing')
		.setDescription('Will he sing a song?'),
	async execute(interaction) {
		await interaction.reply(lyrics);
	},
};
