# Face Attendance App

This project provides a face recognition-based attendance system. GitHub Actions is used to build executable files for Windows and macOS. Pre-built binaries for Linux and macOS are also available for download.

## Repository
GitHub: [FaceAttendanceApp](https://github.com/luongjuan123/FaceAttendanceApp)

## Build the Application

### Build for Windows
- **Workflow:** `.github/workflows/build-windows.yml`
- **Executable File:** `dist/main.exe`

#### How to Run:
1. Extract `face-attendance-app-windows.zip`.
2. Double-click `main.exe`.
3. If Windows shows a security warning, click **"More info"** > **"Run anyway"**.

---

### Build for macOS
- **Workflow:** `.github/workflows/build-macos.yml`
- **Executable File:** `dist/main`
- **Download Pre-built Binary:** [macOS Binary](https://drive.google.com/file/d/1dMH0yDGDLSJ3qCvQjHpYlM0LlRSV6-ox/view?usp=drive_link)

#### How to Run:
1. Extract `face-attendance-app-macos.zip`.
2. Run in terminal:
   ```sh
   ./main
   ```
3. If macOS flags it as an **"unidentified developer"**, go to:
   - **System Preferences** > **Security & Privacy** > **"Open Anyway"**.

---

### Build for Ubuntu
- **Download Pre-built Binary:** [Ubuntu Binary](https://drive.google.com/file/d/1UQ2MniqlfMueA_o16xDOc5WFI66VOWTF/view?usp=drive_link)

#### How to Run:
1. Extract the downloaded archive (e.g., `face-attendance-app-linux.tar.gz`).
2. Run in terminal:
   ```sh
   ./main
   ```
3. Ensure execution permissions:
   ```sh
   chmod +x main
   ```
   if needed.

---

**Default Login Credentials:**
- **Username:** `admin`
- **Password:** `admin`

For any issues, refer to the [documentation](#) or open an [issue](#) on GitHub.

