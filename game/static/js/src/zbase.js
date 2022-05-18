export class AcGame
{
    constructor(id, AcOS) 
    {
        //console.log("This is a test!");
        this.id = id;
        this.$ac_game = $('#' + id);
        this.AcOS = AcOS;

        this.settings = new Settings(this);
        this.menu = new AcGameMenu(this);
        this.playground = new AcGamePlayground(this);
        this.start();
    }
    start()
    {
    }
}
