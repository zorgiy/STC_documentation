$(document).ready(function () {
    window.setTimeout(function() {
        $(".alert").fadeTo(500, 0).slideUp(500, function(){
            $(this).remove();
        });
    }, 2000);
});

$(document).ready(function() {
    $('.button_table').on('click', function(e) {
        e.preventDefault();

        var url = $(this).data('url');
        $.get(url, function(data) {
            var modal = $('<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false"\n' +
                '                 tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true"></div>');
            var modalDialog = $('<div class="modal-dialog modal-dialog-centered"></div>');
            var modalContent = $('<div class="modal-content"></div>');
            var modalHeader = $('<div class="modal-header">' +
                '<h1 class="modal-title fs-5">Редактирование</h1>' +
                '<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button></div>');
            var modalBody = $('<div class="modal-body"></div>');
            var modalFooter = $('<div class="modal-footer">' +
                '<button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Закрыть</button>' +
                '<button form="update_data" type="submit" class="btn btn-secondary btn-sm">Обновить</button></div>');
            var form = $(data).find('#update_data');
            modalBody.append(form);
            modalContent.append(modalHeader);
            modalContent.append(modalBody);
            modalContent.append(modalFooter);
            modalDialog.append(modalContent);
            modal.append(modalDialog);
            $('body').append(modal);

            modal.modal('show');

            form.on('submit', function(e) {
                e.preventDefault();

                var formData = $(this).serialize();
                $.post(url, formData, function(data) {
                    modal.modal('hide');
                    // Получаем элемент редактируемой строки
                    var editedRow = $('.button_table[data-url="' + url + '"]').closest('tr');
                    // Добавляем к элементу класс, меняющий цвет фона
                    editedRow.addClass('table-active');
                    // Обновляем страницу после задержки, чтобы изменения были заметны
                    setTimeout(function() {
                        location.reload();
                    }, 2000);
                });
            });
        });
    });
});
$(document).ready(function() {
    $('.partners-select2').select2({
        language: 'ru',
        width: '90%',
        placeholder: 'Контрагент'
    });
});
$(document).ready(function() {
    $('.signed-select2').select2({
        language: 'ru',
        width: '100%',
        placeholder: 'Подписал'
    });
});
$(document).ready(function() {
    $('.author-select2').select2({
        language: 'ru',
        width: '100%',
        placeholder: 'Исполнитель'
    });
});
$(document).ready(function() {
    $('.workers-select2').select2({
        language: 'ru',
        width: '100%',
        placeholder: 'Сотрудник'
    });
});
