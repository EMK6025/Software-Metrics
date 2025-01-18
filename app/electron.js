import { app, BrowserWindow, ipcMain } from 'electron/main';
import path from 'node:path';
import url from 'node:url';
import sqlite3 from 'sqlite3';

// __dirname is not automatically available with ES modules
const __dirname = path.dirname(url.fileURLToPath(import.meta.url));

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    autoHideMenuBar: true, 
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // Load the preload script
      contextIsolation: true,
    },
  });

  mainWindow.loadURL('http://localhost:3000');
  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

ipcMain.handle('fetch-data', async () => {
  return new Promise((resolve, reject) => {
    const dbPath = path.join(__dirname, 'backend/database.db');
    const db = new sqlite3.Database(dbPath);

    db.all('SELECT * FROM projects', (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
      db.close();
    });
  });
});

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});