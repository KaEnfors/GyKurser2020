

function stopAnim() {
    
    console.error("Stop!") //Printar "stop"

    // Hämtar lista med alla element i sidan
    // som har classen "logo-anim"
    anims = document.getElementsByClassName('logo-anim')
    
    
    while (anims.length > 0) {
        
        console.log("Current anims:", anims)
        // Ta bort classe logo-anim
        // ...lägg till class logo-anim-stopped
        anims[0].classList.add('logo-anim-stopped');
        anims[0].classList.remove('logo-anim');

        //anims[0].style.backgroundColor = 'red'


    }

    banner = document.getElementById("banner")
    banner.classList.add('opacity-low')

    allDivs = document.getElementsByTagName('div')
    console.log("All divs:", allDivs)

}
function playAnim() {
    

    console.log("Play!")

    // Hämtar lista med alla element i sidan
    // som har classen "logo-anim"
    anims = document.getElementsByClassName('logo-anim-stopped')
    /**
     * anims = [
     *  html-sak,
     *  annan html-sak,
     *  ...,
     *  ...
     * ]

     */
    console.log("Found anims:", anims)

    while (anims.length > 0) {
        
        // Ta bort classe logo-anim
        // ...lägg till class logo-anim-stopped
        anims[0].classList.add('logo-anim')
        anims[0].classList.remove('logo-anim-stopped')
    }

}


function changeBgColor(){
    //Changes color of elements....

    mySideContent = document.getElementById('side-content');
    mySideContent.style.backgroundColor = "blue";
    console.log(mySideContent.innerHTML);


}


