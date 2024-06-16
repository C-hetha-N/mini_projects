document.addEventListener("DOMContentLoaded", () => {

    let con = document.querySelector(".container");
    let msgs = con.children;

    function ShowMsg(index) {
        let msg = msgs[index]
        if (index > 0) {
            msgs[index - 1].querySelector(".dots").classList.remove("blink")
        }

        if (index < msgs.length) {
            msg.style.display = 'block';
            msg.querySelector(".dots").classList.add("blink")
            let delay = Math.ceil(2000 + Math.random() * 10000)
            console.log(delay);
            setTimeout(() => {
                ShowMsg(index + 1);
            }, delay);
        }
    }

    con.style.display = 'flex';
    ShowMsg(0)

})
