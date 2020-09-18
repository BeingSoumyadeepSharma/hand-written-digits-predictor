window.addEventListener('load', ()=>{ 
    document.addEventListener('mousedown', startPainting); 
    document.addEventListener('mouseup', stopPainting); 
    document.addEventListener('mousemove', sketch);
});

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext('2d');

let clearBTN = document.getElementById("clearBTN");
let submitBTN = document.getElementById("submitBTN");
let result = document.getElementById("result")

let coord = {x:0 , y:0};

let paint = false;

ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

function getPosition(event) {
    coord.x = event.clientX - canvas.offsetLeft;
    coord.y = event.clientY - canvas.offsetTop;
}

function startPainting(event) {
    paint = true;
    getPosition(event);
}

function stopPainting() {
    paint = false;
}

function sketch(event) {
    if (!paint) return;
    ctx.beginPath();

    ctx.lineWidth = 35;

    ctx.lineCap = 'round';

    ctx.strokeStyle = 'black'

    ctx.moveTo(coord.x, coord.y);

    getPosition(event);

    ctx.lineTo(coord.x, coord.y);

    ctx.stroke();
}

/*
let convertCanvasToImage = (canvas) => {
    let image = new Image();
    image.src = canvas.toDataURL("image/jpeg", 1.0);
    return image;
};
*/

clearBTN.addEventListener('click', function(event) {
    window.location.reload()
    //ctx.clearRect(0, 0, canvas.width, canvas.height);
}, false);

submitBTN.addEventListener('click', function(event) {
    let dataURL = canvas.toDataURL("image/png", 1.0);
    /*
    let canvasImg = convertCanvasToImage(canvas);
    */
    fetch(`${window.origin}/`, {
        method: 'POST',
        body: dataURL
    })
        .then(function(response) { return response.json() })
        .then(function(obj) { 
            let div = `<span>${obj.data}</span>`; 
            result.innerHTML = div; 
        })
        .catch(function(err) { console.log(err) });
}, false);
