clearSelectbox = (selectbox) ->    # 删除options
    len = selectbox.options.length    # 注意删除操作不能放在循环里计算长度
    for i in [0...len]   # three dots [ ), .. means [], 三个点点是左闭右开
        selectbox.remove(0)


$(document).ready ->
    s = ""
    if s
        console.log 'hehe'
    sel = $('#selLocation').get(0)
    clearSelectbox(sel)
