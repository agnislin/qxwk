document.querySelectorAll("[id$=-a]").forEach( panal =>{
    panal.onclick = () => {
        document.querySelectorAll("[id$=-panal]").forEach( p =>{
            p.style.display = "none";
        });

        const panal_name = panal.id.split("-")[0];
        pid = "#"+panal_name+"-panal";
        document.querySelector(pid).style.display = "block";
    }
});
