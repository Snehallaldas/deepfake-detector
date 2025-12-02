const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");
const loader = document.getElementById("loader");
const resultBox = document.getElementById("resultBox");
const resultLabel = document.getElementById("resultLabel");
const realBar = document.getElementById("realBar");
const fakeBar = document.getElementById("fakeBar");

let selectedFile = null;

/* Drag & Drop */
dropArea.onclick = () => fileInput.click();
fileInput.onchange = () => handleFile(fileInput.files[0]);

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.style.background = "rgba(255,255,255,0.15)";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.style.background = "transparent";
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.style.background = "transparent";
    handleFile(e.dataTransfer.files[0]);
});

/* Handle File */
function handleFile(file) {
    selectedFile = file;
    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
        resultBox.style.display = "none";
    }
    analyzeImage();
}

/* Send to backend */
async function analyzeImage() {
    if (!selectedFile) return;

    loader.style.display = "block";

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
        const res = await fetch("https://deepfake-detector-wmdv.onrender.com/predict", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        loader.style.display = "none";
        resultBox.style.display = "block";

        // Label styling
        resultLabel.textContent = `Result: ${data.label}`;
        resultLabel.style.color = data.label === "REAL" ? "#00c853" : "#d50000";

        // Progress bars
        realBar.style.width = (data.real_probability * 100).toFixed(1) + "%";
        fakeBar.style.width = (data.fake_probability * 100).toFixed(1) + "%";

    } catch (error) {
        loader.style.display = "none";
        alert("Backend not reachable.");
    }
}
