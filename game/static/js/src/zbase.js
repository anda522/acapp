export class AcGame {
   constructor(id) {
       console.log("This is a test!");
       this.id = id;
       this.$ac_game = $('#' + id);
       this.menu = new AcGameMenu(this);
       this.playground = new AcGamePlayground(this);
       this.start();
   }
    start(){
    }
}
