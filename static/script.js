document.getElementById('turn').addEventListener('click', async function() {
    await turn();
});

async function turn() {
    const response = await fetch('/turn', { method: 'POST' });
    const data = await response.json();
    
    updatePanels(data.new_faces);
}

function updatePanels(newFaces) {
    for (let face in newFaces) {
        const panels = newFaces[face];
        for (let i = 0; i < panels.length; i++) {
            const panelElement = document.getElementById(`${face}${i}`);
            if (panelElement) {
                panelElement.style.background = panels[i];
            }
        }
    }
}

