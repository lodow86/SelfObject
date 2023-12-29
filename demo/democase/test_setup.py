#
#
# 模块级：setup_module()/teardown_module()：开始于模块始末，全局的。
# 函数级：setup_function()/teardown_function()：只对函数用例生效（不在类中）。
# 类级与方法级，定义在类中
#
# 类级：setup_class()/teardown_class()：只在类中前后运行一次(在类中)。
#
# 方法级：setup_method()/teardown_method()：开始于方法始末（在类中）。
#
# 自由的：setup()/teardown()：直接使用感觉和方法级前后置函数一样。
