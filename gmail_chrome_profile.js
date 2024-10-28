const puppeteer = require('puppeteer-extra');
const pluginStealth = require("puppeteer-extra-plugin-stealth");
const axios = require('axios');
const path = require('path');

const fs = require('fs');
const args = process.argv.slice(2);
const profile = args[0];
const port = args[1]
console.log(profile);
console.log(port)
const { exec } = require('child_process');
text = '';
// let keywordsFromFile;
// try {
//     keywordsFromFile = fs.readFileSync(filePath, 'utf-8').split('\n').map(keyword => keyword.trim());
// } catch (error) {
//     console.error('Error reading the file:', error);
// }

(async () => {
    try {
        puppeteer.use(pluginStealth());

        // Step 1: Launch Chrome with remote debugging port using child_process
        const chromePath = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"';
        const userDataDir = `"C:\\Users\\Naveed\\AppData\\Local\\Google\\Chrome\\User Data\\Profile ${profile}"`;
        const remoteDebuggingPort = port;


        // Command to launch Chrome
        //to view the browser
        const chromeLaunchCommand = `${chromePath} --remote-debugging-port=${remoteDebuggingPort} --user-data-dir=${userDataDir}`;
        //to hide the browser
        //const chromeLaunchCommand = `${chromePath} --headless --remote-debugging-port=${remoteDebuggingPort} --user-data-dir=${userDataDir}`;

        // Run the Chrome instance
        exec(chromeLaunchCommand, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error launching Chrome: ${error.message}`);
                return;
            }
            console.log('Chrome launched successfully!');
        });

        // Wait a few seconds to allow Chrome to launch
        await new Promise(resolve => setTimeout(resolve, 3000));

        // Step 2: Connect Puppeteer to the running Chrome instance
        const response = await axios.get(`http://127.0.0.1:${remoteDebuggingPort}/json/version`);
        const { webSocketDebuggerUrl } = response.data;

        const browser = await puppeteer.connect({
            browserWSEndpoint: webSocketDebuggerUrl,
            ignoreHTTPSErrors: true,
            defaultViewport: null,
            headless: true,  // Run in headless mode
            args: ['--start-maximized']  // Keep this if you want window maximized even in headless mode
        });


        console.log(await browser.pages());  // Log currently open pages

        // Step 3: Open a new page and automate Gmail login
        const page = await browser.newPage();

        // Wait before navigating
        await new Promise(resolve => setTimeout(resolve, 2000));

        // Attempt to navigate with retries
        try {
            await page.goto('https://www.facebook.com/messages', { waitUntil: 'networkidle2', timeout: 120000 });
        } catch (error) {
            console.log('Navigation timeout or error:', error);
        }

        await new Promise(resolve => setTimeout(resolve, 2000));
        const checkKeywords = ['yes', 'sure', 'yeah', 'here is our website', 'www'];
        let mergedTextContent = ['Sent', 'You sent', 'Enter', 'Facebook', 'end-to-end encrypted', 'Messages and calls are secured with end-to-end encryption. Learn more','00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'];
    }
    catch(e){

    }
})()