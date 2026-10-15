/**
 * 班级学生信息管理系统 - 自定义 JavaScript
 * Django + Bootstrap 4
 */

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function () {
    'use strict';

    // ==================== Bootstrap 表单验证 ====================
    (function () {
        var forms = document.getElementsByClassName('needs-validation');
        Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    })();

    // ==================== 警告框自动消失 ====================
    (function () {
        var alerts = document.querySelectorAll('.alert-dismissible');
        alerts.forEach(function (alert) {
            // 5秒后自动关闭
            setTimeout(function () {
                var closeBtn = alert.querySelector('.close');
                if (closeBtn) {
                    closeBtn.click();
                }
            }, 5000);
        });
    })();

    // ==================== 表格行点击高亮 ====================
    (function () {
        var tableRows = document.querySelectorAll('.table-hover tbody tr');
        tableRows.forEach(function (row) {
            row.addEventListener('click', function () {
                tableRows.forEach(function (r) {
                    r.classList.remove('table-active');
                });
                this.classList.add('table-active');
            });
        });
    })();

    // ==================== 学号输入限制 ====================
    (function () {
        var sidInput = document.querySelector('input[name="student_id"]');
        if (sidInput) {
            sidInput.addEventListener('input', function () {
                // 只允许输入数字
                this.value = this.value.replace(/\D/g, '');
                // 限制8位
                if (this.value.length > 8) {
                    this.value = this.value.slice(0, 8);
                }
            });
        }
    })();

    // ==================== 删除按钮二次确认 ====================
    (function () {
        var deleteLinks = document.querySelectorAll('a[href*="delete"]');
        deleteLinks.forEach(function (link) {
            link.addEventListener('click', function (event) {
                // 对于列表中的删除链接，跳转到确认页面即可（无需额外拦截）
                // 此处的链接自然指向确认页面
            });
        });
    })();

    // ==================== 控制台欢迎信息 ====================
    console.log('欢迎使用班级学生信息管理系统！');
    console.log('技术栈：Django 2.2 + Bootstrap 4 + jQuery');
    console.log('© 2026 计科231-2311');
});
