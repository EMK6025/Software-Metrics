import { app, BrowserWindow } from 'electron/main';
import path from 'node:path';
import url from 'node:url';

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