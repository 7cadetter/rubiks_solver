async function turn(direction) {
    const response = await fetch(`/turn?direction=${direction}`, { method: 'POST' });
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

async function setPanel(panel, colour) {
    const response = await fetch(`/set?panel=${panel}&colour=${colour}`, { method: 'POST' });
    const data = await response.json();
}

async function reset() {
    const response = await fetch(`/reset`, { method: 'POST' });
    const data = await response.json();
    updatePanels(data.new_faces);
}

async function solve() {
    const response = await fetch(`/solve`, { method: 'POST' });
    const data = await response.json();
    window.location.href = data.redirect_url;
}

let current_colour = '';

document.getElementById('rightface').addEventListener('click', () => turn('left'));
document.getElementById('leftface').addEventListener('click', () => turn('right'));
document.getElementById('topface').addEventListener('click', () => turn('forward'));
document.getElementById('bottomface').addEventListener('click', () => turn('backward'));
document.getElementById('backface').addEventListener('click', () => turn('switch'));
document.getElementById('counter').addEventListener('click', () => turn('counter'));
document.getElementById('clockwise').addEventListener('click', () => turn('clockwise'));

document.getElementById('reset').addEventListener('click', () => reset())

document.getElementById('solve').addEventListener('click', () => solve())

const colours = document.querySelectorAll('.colour');
colours.forEach(colour => {
    colour.addEventListener('click', () => {
        current_colour = colour.id;});
})

const panels = document.querySelectorAll('.panel');
panels.forEach(panel => {
    panel.addEventListener('click', () => {
        if (current_colour && panel.id != 'front8') {
            panel.style.background = current_colour;
            setPanel(panel.id, current_colour)
        }
    });
});



