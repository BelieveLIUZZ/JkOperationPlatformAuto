# JkOperationPlatformAuto
JK运营平台自动化测试脚本框架，适用于web项目使用

        ----------------------------------
        --  参考示例：                    --
        --      data:                   --
        --          baidu_search.csv    --
        --      pages:                  --
        --          baidu_page.py       --
        --      testscipts:             --
        --          test_baidu.py       --
        ----------------------------------

    项目框架内容详解：
            base_framework
                    自定义封装的类：
                    base_analyze.py                    -------解析参数化文件的类
                    base_page.py                        -------页面基类
                    browser_engine.py                 -------浏览器驱动类
                    logger.py                               -------日志类
            configs
                    auto_login.ini
                    config.ini
            data
                    data.csv
                    data.json
                    data.txt

            function
                    常用函数(针对用例的期望和实际结果的对比)

            logs
                生成的日志文件


            pages
                login_page.py
                main_page.py
                page.py                        --------所有页面的入口(后期页面较多时，page可以作为所有页面的统一入口，简洁，方便)

            reports
                生成的测试报告(目前使用的HTMLTestReportCN.py中文版的测试报告)
                2018-09-30_10_23HTMLTestTemplate.html

            screenshots
                生成的截图 .png  占用内存比较小
                2018-09-30_11_23.png

            sys_tools
                系统的工具文件，修改了内容，里面做了对应的注释
                HTMLTestReportCN.py            ----生成HTML测试报告(中文)
                            ***内容在原来基础上做了修改，目前使用中文的饼状和表格都支持,增加的饼状图有对应的注释
                HTMLTestRunner.py                ----生成HTML测试报告(英文)

            testscripts
                make_report.py                     ----生成表格测试报告类
                    ** 两种方式 组合测试套件的方式 并生成测试报告
                make_report_pie.py               ----生成饼状+表格测试报告类
                   test_login_analyze.py              ---- 关于如何解析数据CSV文件(参照此类)
                test_login.py
                test_main.py


              -----------------------------------
                test_login_to_logout.py                登录成功and退出
                test_login_analyze.py                   登录 包括解析csv文件和执行多个登录相关用例(demo)

                test_home_login.py                      登录时包含的几种情况，用户名不存在、密码错误等

                test_dept_manage.py                    系统管理-->部门管理：筛选查询(模糊和精确)

                测试报告演示：result.html
              -----------------------------------

