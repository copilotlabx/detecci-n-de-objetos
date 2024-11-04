const startButton = document.getElementById("start-button");
const captureResults = document.getElementById("capture-results");

startButton.addEventListener("click", () => {
    setInterval(fetchData, 2000);  // Actualizar cada 2 segundos
});

function fetchData() {
    fetch("data.json")
        .then(response => response.json())
        .then(data => {
            captureResults.innerHTML = "";  // Limpia fotogramas anteriores
            data.frames.forEach(frameData => {
                const frameDiv = document.createElement("div");
                frameDiv.classList.add("frame");

                const img = document.createElement("img");
                img.src = frameData.image_url;

                const labelDiv = document.createElement("div");
                labelDiv.classList.add("label");
                labelDiv.textContent = `${frameData.label} (${frameData.confidence}%)`;

                frameDiv.appendChild(img);
                frameDiv.appendChild(labelDiv);
                captureResults.appendChild(frameDiv);
            });
        })
        .catch(error => console.error("Error al capturar fotogramas:", error));
}
