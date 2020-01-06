var liste = [];

function add() {
	var shto = prompt("Shkruani emrin e nje personi qe deshironi te shtoni")
	liste.push(shto)
}

function display() {
	console.log(liste);
}

function remove() {
	var hiq = prompt("Shkruani emrin e personit qe deshironi te hiqni")
	var index = liste.indexOf(hiq); //Kjo tregon indeksin e variablit hiq ne arrayn me emrin liste
	liste.splice(index,1); //Kjo heq nga indeksi e mbrapa 1 element. ne rastin tone heq vete indeksin
}
var admin = prompt("Deshironi te logoheni si admin? Y/N");
var menu = "";
if (admin == "y") {
	while (menu != "quit") {
		menu = prompt("Zgjidhni nje nga menute: Add/Dipslay/Remove or /Quit to Exit!");
		if (menu == "add") {
			add();
		}else if (menu == "display") {
			display();
		}else if(menu == "remove"){
			remove();
		}else {
			alert("Je jasht binarsh")
		}
	}
}
