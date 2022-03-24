const btn = this.document.querySelector('#btn')
const { remote } = require('electron')
const BrowserWindow = remote.BrowserWindow

window.onload = function(){
   btn.onclick = ()=>{

        newWin = new BrowserWindow({
            width:500,
            height:500,
        })
        newWin.loadFile('yellow.html')
        newWin.on('closed',()=>{ newWin = null })

    }
}

var rigthTemplate = [
    {label:'粘贴'},
    {label:'复制'}
]

var m = remote.Menu.buildFromTemplate(rigthTemplate)

window.addEventListener('contextmenu',function(e){

  //阻止当前窗口默认事件
  e.preventDefault();
  //把菜单模板添加到右键菜单
  m.popup({window:remote.getCurrentWindow()})

})