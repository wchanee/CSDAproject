let records = [];
let currentImage = null;

document.addEventListener('DOMContentLoaded', function () {
    const imageUpload = document.getElementById('imageUpload');
    const fileName = document.getElementById('fileName');
    const previewImage = document.getElementById('previewImage');
    const resultImage = document.getElementById('resultImage');
    const analyzeButton = document.getElementById('analyzeButton');
    const emptySpaces = document.getElementById('emptySpaces');
    const occupiedSpaces = document.getElementById('occupiedSpaces');
    const totalSpaces = document.getElementById('totalSpaces');
    const recordsList = document.getElementById('recordsList');

    imageUpload.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file) {
            fileName.textContent = file.name;
            const reader = new FileReader();
            reader.onload = function (e) {
                currentImage = e.target.result;
                previewImage.src = currentImage;
                previewImage.style.display = 'block';
                resultImage.style.display = 'none';
                analyzeButton.disabled = false;
            };
            reader.readAsDataURL(file);
        }
    });

    analyzeButton.addEventListener('click', function () {
        detectCars();
    });

    async function detectCars() {
        if (!currentImage) {
            alert('Please select an image or wait for a random image to load.');
            return;
        }

        try {
            analyzeButton.disabled = true;
            analyzeButton.textContent = 'Detecting...';

            const response = await fetch('/detect', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ image: currentImage })
            });
            const data = await response.json();

            updateCurrentStats(data);
            saveRecord(data.occupied_spaces, data.empty_spaces, data.total_spaces);

            resultImage.src = data.image;
            resultImage.style.display = 'block';

            analyzeButton.textContent = 'Detect Cars';
            analyzeButton.disabled = false;
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during detection.');
            analyzeButton.textContent = 'Detect Cars';
            analyzeButton.disabled = false;
        }
    }

    function saveRecord(occupiedSpaces, emptySpaces, totalSpaces) {
        const now = new Date();
        const record = {
            timestamp: now.toLocaleString(),
            occupiedSpaces: occupiedSpaces,
            emptySpaces: emptySpaces,
            totalSpaces: totalSpaces
        };
        records.unshift(record);
        if (records.length > 5) records.pop();
        updateRecordsList();
    }

    function updateRecordsList() {
        recordsList.innerHTML = records.map(record => `
            <div class="record">
                <p><strong>${record.timestamp}</strong></p>
                <p>Empty Spaces: ${record.emptySpaces}</p>
                <p>Occupied Spaces: ${record.occupiedSpaces}</p>
                <p>Total Car Spaces: ${record.totalSpaces}</p>
            </div>
        `).join('');
    }

    function updateCurrentStats(data) {
        emptySpaces.textContent = data.empty_spaces;
        occupiedSpaces.textContent = data.occupied_spaces;
        totalSpaces.textContent = data.total_spaces;
    }
});
