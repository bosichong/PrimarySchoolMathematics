var psm_app = {} //命名一个自己用的空间
psm_app.psminfo = ""//口算题内容提示文字
psm_a = new Array()//口算题参数数组
psm_b = {} //剩余参数


$(document).ready(function () {

    // 加载APP配置并渲染页面
    $.getJSON("./api_getConfigJson",
        function (data, textStatus, jqXHR) {
            appconfig = data; // 加载APP配置
            psm_app.config = appconfig.config //保存配置稍后使用
            // alert(appconfig.config[9][0][1])
            $("#signum" + appconfig.config.signum).attr("checked", true); //选择运算类型
            $("#step" + appconfig.config.step).attr("checked", true); //选择几步运算
            $("#is_result" + appconfig.config.is_result).attr("checked", true); //题型设置
            $("#carry" + appconfig.config.add.carry).attr("checked", true); //加法设置
            $("#abdication" + appconfig.config.sub.abdication).attr("checked", true); //减法设置
            $("#remainder" + appconfig.config.div.remainder).attr("checked", true); //减法设置

            // 运算项及结果范围数值设置
            $("#multistep_a1").attr("value", appconfig.config.multistep[0][0]);
            $("#multistep_a2").attr("value", appconfig.config.multistep[0][1]);

            $("#multistep_b1").attr("value", appconfig.config.multistep[1][0]);
            $("#multistep_b2").attr("value", appconfig.config.multistep[1][1]);

            $("#multistep_c1").attr("value", appconfig.config.multistep[2][0]);
            $("#multistep_c2").attr("value", appconfig.config.multistep[2][1]);

            $("#multistep_d1").attr("value", appconfig.config.multistep[3][0]);
            $("#multistep_d2").attr("value", appconfig.config.multistep[3][1]);

            $("#multistep_e1").attr("value", appconfig.config.multistep[4][0]);
            $("#multistep_e2").attr("value", appconfig.config.multistep[4][1]);

            //运算符号的选择
            for (let i = 0; i < appconfig.config.symbols[0].length; i++) {
                $("#symbols_a" + appconfig.config.symbols[0][i]).attr("checked", true); //第一处
            }

            for (let i = 0; i < appconfig.config.symbols[1].length; i++) {
                $("#symbols_b" + appconfig.config.symbols[1][i]).attr("checked", true); //第二处
            }

            for (let i = 0; i < appconfig.config.symbols[2].length; i++) {
                $("#symbols_c" + appconfig.config.symbols[2][i]).attr("checked", true); //第三处
            }

            //口算卷子设置
            $("#juanzishu").attr("value", appconfig.config.juanzishu);
            $("#lieshu").attr("value", appconfig.config.lieshu);
            $("#jz_title").attr("value", appconfig.config.jz_title);
            $("#inf_title").attr("value", appconfig.config.inf_title);
            $("#number").attr("value", appconfig.config.number);
            $("#docx").attr("value", appconfig.config.docx);

            if (appconfig.config.is_bracket == 1) {
                $("#is_bracket").attr("checked", true);

            } else {
                $("#is_bracket").attr("checked", false);
            }

        }
    );


    //点击添加口算题按钮
    $("#addpsm").click(function (e) {
        createPSM()
    });
    //清空当前口算题
    $("#cleanpsm").click(function (e) {
        $("#psmtextarea").val("")
        psm_a.length = 0//清空参数数组
        psm_app.psminfo = "" //清空提示文字

    });

    //提交最后的参数，生成口算题
    $('#psmsubmit').click(function (e) {

        producePSM()


    });


    function producePSM() {
        /**
         * 为生成最后的口算题提交参数
         */

        //拼装剩余参数

        psm_b.juanzishu = parseInt($('#juanzishu').val())
        psm_b.lieshu = parseInt($('#lieshu').val())
        psm_b.docx = $('#docx').val()
        psm_b.jz_title = $('#jz_title').val()
        psm_b.inf_title = $('#inf_title').val()
        psm_data = [psm_a, psm_b]

        $.ajax({
            type: "POST",
            url: "./api_producePSM",
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify(psm_data),
            dataType: "json",
            success: function (message) {

                if (message["info"] != '0') {
                    if (psm_a.length > 0) {
                        $(".psminfo").text(message["info"])
                        // alert(message["info"])
                        $('#exampleModal').modal("show")
                    }else{
                        $(".psminfo").text("当前口算题没有任何内容，请添加口算后在生成！")
                        // alert(message["info"])
                        $('#exampleModal').modal("show")
                    }



                }
                else {
                    alert("口算题生成失败！请重新设置程序参数！");
                }


            },
            error: function (message) {
                alert("提交失败" + JSON.stringify(message));
            }
        });



    }

    function createPSM() {
        /**
         * 创建一组口算题的配置（为当前口算题添加内容）
         */

        psm_tmp = {}
        psm_tmp.signum = parseInt($('input[name="signum"]:checked').val())
        psm_tmp.step = parseInt($('input[name="step"]:checked').val())
        psm_tmp.number = parseInt($('#number').val())
        psm_tmp.is_result = parseInt($('input[name="is_result"]:checked').val())
        if ($('#is_bracket').prop("checked")) {
            psm_tmp.is_bracket = 1
        } else {
            psm_tmp.is_bracket = 0
        }


        psm_tmp.add = {
            "carry": parseInt($('input[name="carry"]:checked').val())
        }
        psm_tmp.sub = {
            "abdication": parseInt($('input[name="abdication"]:checked').val())
        }
        psm_tmp.mult = {}
        psm_tmp.div = {
            "remainder": parseInt($('input[name="remainder"]:checked').val())
        }

        psm_tmp.multistep = [
            [parseInt($("#multistep_a1").val()), parseInt($("#multistep_a2").val()),],
            [parseInt($("#multistep_b1").val()), parseInt($("#multistep_b2").val()),],
            [parseInt($("#multistep_c1").val()), parseInt($("#multistep_c2").val()),],
            [parseInt($("#multistep_d1").val()), parseInt($("#multistep_d2").val()),],
            [parseInt($("#multistep_e1").val()), parseInt($("#multistep_e2").val()),]
        ]
        ss_a = new Array()
        $('input[name="symbols_a"]').each(function (index, element) {
            if ($(this).prop("checked")) {
                // alert($(this).val())
                ss_a.push(parseInt($(this).val()))
            }
        });
        ss_b = new Array()
        $('input[name="symbols_b"]').each(function (index, element) {
            if ($(this).prop("checked")) {
                // alert($(this).val())
                ss_b.push(parseInt($(this).val()))
            }
        });
        ss_c = new Array()
        $('input[name="symbols_c"]').each(function (index, element) {
            if ($(this).prop("checked")) {
                // alert($(this).val())
                ss_c.push(parseInt($(this).val()))
            }
        });

        psm_tmp.symbols = [ss_a, ss_b, ss_c]


        $.ajax({
            type: "POST",
            url: "./api_createPSM",
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify(psm_tmp),
            dataType: "json",
            success: function (message) {

                if (message["info"] != '0') {
                    psm_app.psminfo += message["info"]
                    psm_a.push(psm_tmp)
                    $("#psmtextarea").val(psm_app.psminfo)
                }
                else {
                    if (psm_tmp.is_result == 1 || psm_tmp.step >1){
                        // alert("如果题型为求算数项或是多步运算时，除法结果则不能选择有余数！")
                        $(".psminfo").text("如果题型为求算数项或是多步运算时，除法结果则不能选择有余数！")
                        // alert(message["info"])
                        $('#exampleModal').modal("show")
                    }else{
                        // alert("除数不能为0!请修改运算项范围数值设置！")
                        $(".psminfo").text("除数不能为0!请修改运算项范围数值设置！")
                        // alert(message["info"])
                        $('#exampleModal').modal("show")
                    }
                }


            },
            error: function (message) {
                alert("提交失败" + JSON.stringify(message));
            }
        });







    }


});