/**
 * Created by lixing on 2018/1/2.
 */

/**
 * 提交用户选中的图片
 * @param id
 */
function choose(id){
//    alert(id);
    document.getElementById("favorPhoto").value = id;
    document.forms[0].submit();
}