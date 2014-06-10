$(document).ready(function(){
    $('#myTable').dataTable({
    language: {
        processing:     "Processando....",
        search:         "Busque em todos os campos",
        lengthMenu:    "Mostre _MENU_ escolas",
        info:           "Disponibilizadas as escolas de _START_ a; _END_ em _TOTAL_ escolas disponiveis",
        infoEmpty:      "A escola selecionada nao possui escolas com o mesmo perfil",
        infoFiltered:   "(Disponibilizado  _MAX_ escolas em relacao ao total)",
        infoPostFix:    "",
        loadingRecords: "Carregamento em processo...",
        zeroRecords:    "O termo da busca nao foi encontrado",
        emptyTable:     "A escola selecionada nao possui escolas com o mesmo perfil",
        paginate: {
            first:      "Primeiro",
            previous:   "Anterior",
            next:       "Proximo",
            last:       "Ultimo"
        },
        aria: {
            sortAscending:  ":Tabela ordenada de maneira crescente",
            sortDescending: ": Tabela ordenada de maneira decrescente"
        }
    }
});
});