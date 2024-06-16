console.log("ScriptEx13.js is intilaizing.....")

console.log("createCard(title, cName, views, monthsOld, duration, thumbnail)");
console.log("Example : ");
console.log(" createCard(Lets rock it with harry | Sigma web development Course - Tutorial #10", "CodeWithHarry", 84000000, 2, "18:34", "https://i.ytimg.com/vi/R11tvGM3nDY/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLADXI7Md0rzAuheDCLC4QKCHos8EA);");
function createCard(title, cName, views, monthsOld, duration, thumbnail) {

    let viewStr;
    if (views < 1000) {
        viewStr = views;
    }
    else if (views < 1000000) {
        viewStr = views / 1000 + "K";
    }
    else if (views < 1000000000) {
        viewStr = views / 1000000 + "M";
    }
    else {
        viewStr = views / 1000000000 + "B";
    }

    let html = `    <section class="container">
    <div class="image">
        <img src="${thumbnail}" alt="">
        <div class="durtn">${duration}</div>
    </div>

    <div class="content">
        <div class="titl">${title}</div>
        <div class="info">${cName} • ${viewStr} views • ${monthsOld} months ago</div>
    </div>
</section>`
    document.querySelector(".container").innerHTML = document.querySelector(".container").innerHTML + html;
}

createCard("Life of an Engineering Student in India (Realistic Vlog)", "FMF", 865, 10, "6:39", "https://i.ytimg.com/vi/BCoaRYGw7WE/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLA7KClIj-DOAizvqEny9xlM9RUX3Q");
createCard("Introduction to Backend | Sigma Web Development Course - Tutorial #2", "CodeWithHarry", 764000, 3, "26:18", "thumbnail_Img.webp");
createCard("CommonJs Vs EcamScript Modules | Sigma web development Course - Tutorial #3", "CodeWithHarry", 656000, 2, "17:46", "thumbnail_Img.webp");
createCard("Introduction to Express Js | Sigma web development Course - Tutorial #4", "CodeWithHarry", 1040000000, 2, "20:39", "https://i.ytimg.com/vi/R11tvGM3nDY/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLADXI7Md0rzAuheDCLC4QKCHos8EA");
createCard("Middlewares in Express Js | Sigma web development Course - Tutorial #5", "CodeWithHarry", 1540000, 1, "19:05", "https://i.ytimg.com/vi/VELNPK0dK84/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLAzW8ocjhwslq-Rfsi9k0OvJsggbw");

console.log("Its done")
