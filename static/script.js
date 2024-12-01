async function turn(direction) {
    const response = await fetch(`/turn?direction=${direction}`, { method: 'POST' });
    const data = await response.json();
    updatePanels(data.new_faces);
}

document.getElementById('rightface').addEventListener('click', () => turn('left'));
document.getElementById('leftface').addEventListener('click', () => turn('right'));
document.getElementById('topface').addEventListener('click', () => turn('forward'));
document.getElementById('bottomface').addEventListener('click', () => turn('backward'));
document.getElementById('backface').addEventListener('click', () => turn('switch'));
document.getElementById('counter').addEventListener('click', () => turn('counter'));
document.getElementById('clockwise').addEventListener('click', () => turn('clockwise'));

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

