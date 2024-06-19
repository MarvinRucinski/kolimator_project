var bg = document.getElementById("bg")



function getRandomColor() {
    const opacity = Math.floor(Math.random() * 10).toString(16);
    color = "#BBCCFF" + opacity.padStart(2, "0");
    // console.log(color);
    return color;
}

for (var i = 0; i < 17 * 10; i++) {
    var div = document.createElement("div");
    div.className = "bg-block";
    div.style.backgroundColor = getRandomColor();

    var dot = document.createElement("div");
    dot.className = "bg-dot";
    div.appendChild(dot);

    var corner = document.createElement("div");
    corner.className = "bg-corner";
    div.appendChild(corner);

    var corner2 = document.createElement("div");
    corner2.className = "bg-corner2";
    div.appendChild(corner2);

    bg.appendChild(div);
}