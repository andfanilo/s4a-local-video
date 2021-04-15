import pathlib 
import shutil
import streamlit as st
import streamlit.components.v1 as components

# HACK This only works when we've installed streamlit with pipenv, so the
# permissions during install are the same as the running process
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
# We create a videos directory within the streamlit static asset directory
# and we write output files to it
VIDEOS_PATH = (STREAMLIT_STATIC_PATH / "videos")
if not VIDEOS_PATH.is_dir():
    VIDEOS_PATH.mkdir()

wildlife_video = VIDEOS_PATH / "Wildlife.mp4"
if not wildlife_video.exists():
    shutil.copy("Wildlife.mp4", wildlife_video)  # For newer Python.


def main():
    components.html("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
.main-div h1
{
 font-size: 21px;
}
</style>
  </head>
  <body>
   <div class="main-div">
    <video src = "videos/Wildlife.mp4" width="480" height="360" controls controlsList="nodownload"></video>
<script type="text/javascript">
//Script for disabling right click on mouse
var message="Function Disabled!";
function clickdsb(){
if (event.button==2){
alert(message);
return false;
}
}
function clickbsb(e){
if (document.layers||document.getElementById&&!document.all){
if (e.which==2||e.which==3){
alert(message);
return false;
}
}
}
if (document.layers){
document.captureEvents(Event.MOUSEDOWN);
document.onmousedown=clickbsb;
}
else if (document.all&&!document.getElementById){
document.onmousedown=clickdsb;
}
document.oncontextmenu=new Function("alert(message);return false")
</script>
</div>
</body>
</html>""", width=500, height=500)


if __name__ == "__main__":
    main()
    