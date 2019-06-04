      function cacher(im){
        im.classList.remove('visible');
        im.classList.add('cachee');
      }
      
      function afficher(im){
        im.classList.remove('cachee');
        im.classList.add('visible');
      }

      function suivant(n){
        if(n<5){
          n++;
        }
        else{n=1;
        }
        return n;
      }


      function change_baniere(){

        var tab = document.getElementsByClassName('visible');
       
        n = tab[0].id;
        document.getElementById(n).style.transition = "opacity 2s";
        document.getElementById(suivant(n)).style.transition = "opacity 2s";
        cacher(document.getElementById(n));
        afficher(document.getElementById(suivant(n)));
      
      }

      var chb = setInterval(change_baniere,3000);