import { app, BrowserWindow } from 'electron/main';
import path from 'node:path';
import url from 'node:url';
import { exec } from 'child_process';

// __dirname is not automatically available with ES modules
const __dirname = path.dirname(url.fileURLToPath(import.meta.url));

// Declare mainWindow globally to ensure it can be accessed across functions
let mainWindow;

function createWindow() {
  console.log('Electron is starting...');
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    autoHideMenuBar: true, 
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  mainWindow.loadURL('http://localhost:3000');

  // Handle the window close event
  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

function handlePythonExecution() {
  ipcMain.on("run-python-script", (event, arg) => {
    console.log(`Executing Python script with argument: ${arg}`);
    const scriptPath = path.join(__dirname, 'path/to/your/script.py'); // Adjust script path as needed

    exec(`python ${scriptPath} ${arg}`, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error.message}`);
        event.reply("python-script-response", { error: error.message });
        return;
      }
      if (stderr) {
        console.error(`stderr: ${stderr}`);
        event.reply("python-script-response", { stderr });
        return;
      }
      console.log(`Python script output: ${stdout}`);
      event.reply("python-script-response", { result: stdout });
    });
  });
}


app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    // Recreate the window if all windows are closed (Mac-specific behavior)
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  // Quit the app when all windows are closed (except on macOS)
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

const { ipcMain } = require("electron");
const { exec } = require("child_process");
