# Face Attendance App

This project provides a face recognition-based attendance system. GitHub Actions is used to build executable files for Windows, Linux and macOS. Pre-built binaries for Linux and macOS are also available for download.

## Repository
GitHub: [FaceAttendanceApp](https://github.com/luongjuan123/FaceAttendanceApp)

## Build the Application

### Build for Windows(now in trouble)
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
- **Download Pre-built Binary:** [macOS Binary](https://drive.google.com/file/d/1ToMDwk1LMXgbIjicRVhtELnVPrP5W450/view?usp=sharing)

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
- **Download Pre-built Binary:** [Ubuntu Binary](https://drive.google.com/file/d/1_dVqmwyCt6iB8FlrUM5F0e7m6B_znBEt/view?usp=sharing)

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



