//Foto Box
const FotoBox = () => {
  //Elements to hide
  const nav = document.querySelector("nav");
  const hamburgerMenu = document.querySelector("#hamburger-menu");
  const baner = document.querySelector("#baner");
  const main = document.querySelector("main");
  const footer = document.querySelector("footer");
  //Element to show
  const fotoBox = document.querySelector(".foto-box");
  const fotoBorder = document.querySelector(".foto-border");
  //Current foto
  const currentFoto = fotoBorder.firstElementChild;

  const exitBox = document.querySelector(".exit-box");
  //Check Element in Array
  const fotoArray = [];
  const fotoGame = document.querySelectorAll(".foto-gallery");
  fotoGame.forEach((foto) => {
    fotoArray.push(foto.getAttribute("src"));

    foto.addEventListener("click", () => {
      let counter = 0;
      const fotoArrayLength = fotoArray.length;
      //Add foto src to current foto div
      currentFoto.src = foto.getAttribute("src");
      //Find src element in array
      /*
        console.log(
          fotoArray.filter((element) => element === foto.getAttribute("src"))
        );
        */
      //Find current foto index in array
      let stratIndexFoto = fotoArray.indexOf(foto.getAttribute("src"));

      //Click events for right button
      fotoBorder.children[3].addEventListener("click", () => {
        counter++;
        let newIndexFoto = stratIndexFoto + counter;
        console.log(newIndexFoto);
        currentFoto.src = fotoArray[newIndexFoto];
        console.log(currentFoto.src);
        if (newIndexFoto === fotoArrayLength) {
          counter = 0;
          stratIndexFoto = 0;
          currentFoto.src = fotoArray[0];
        }
      });

      //Click events for left button
      fotoBorder.children[2].addEventListener("click", () => {
        currentFoto.src =
          fotoArray[fotoArray.indexOf(currentFoto.getAttribute("src")) - 1];
        console.log(
          "Index Src: " +
            fotoArray[fotoArray.indexOf(currentFoto.getAttribute("src"))]
        );
        if (fotoArray.indexOf(currentFoto.getAttribute("src")) < 0) {
          currentFoto.src = fotoArray[fotoArrayLength - 1];
          console.log(fotoArray[fotoArrayLength - 1]);
        }
      });
      //Element Show
      fotoBox.classList.replace("d-none", "d-flex");
      //Element Hide
      nav.style.display = "none";
      hamburgerMenu.classList.replace("d-block", "d-none");
      baner.style.display = "none";
      main.classList.replace("d-flex", "d-none");
      footer.classList.replace("d-flex", "d-none");
    });
  });

  //Exit FotoBox
  exitBox.addEventListener("click", () => {
    //Element Show
    nav.style.display = "block";
    hamburgerMenu.classList.replace("d-none", "d-flex");
    baner.style.display = "block";
    main.classList.replace("d-none", "d-flex");
    footer.classList.replace("d-none", "d-flex");
    //Element Hide
    fotoBox.classList.replace("d-flex", "d-none");
  });
};

FotoBox();
