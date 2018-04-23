function appendRow(parentId, childId) {
    var cloneClub = document.getElementById(parentId);
    console.log(cloneClub.id);
    var cosima = document.getElementById(childId);
    console.log(cosima.id);
    var sarah = cosima.cloneNode(true);
    sarah.id = function() {
        var newId = Math.random().toString(36).replace(/[^a-z]+/g, '').substr(0, 5);
        return newId;
    }();
    var input = sarah.getElementsByTagName("input")[0];
    input.id = [input.id, "-", sarah.id].join('')
    input.value = ''
    console.log(sarah.id);
    cloneClub.append(sarah);
};

window.onload=function() {
    if (document.location.pathname === '/loot-calc') {
        document.getElementById("addMore").addEventListener("click", function() {
            appendRow("loot-form", "row1");
        });
    };
    console.log("onload done");
};

