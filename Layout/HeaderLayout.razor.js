export function onLoad() {
    window.onscroll = function () {
        var header = document.getElementById("header-layout");
        if (window.scrollY > 200) {
            header.classList.add("fixed-top");
            header.classList.add("shadow-xs");
            header.classList.add("bg-body");
        } else {
            header.classList.remove("fixed-top");
            header.classList.remove("shadow-xs");
            header.classList.remove("bg-body");
        }
    };
}
