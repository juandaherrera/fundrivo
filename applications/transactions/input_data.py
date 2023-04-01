currency_instances = {
    'COP' : 'Pesos Colombianos',
    'USD' : 'US Dollar'
}

account_category_instaces = {
    'Cuenta corriente': {
        'description' :  'Esta cuenta se utiliza generalmente para administrar los ingresos y gastos diarios de una empresa o persona. Se puede acceder fácilmente a los fondos, lo que la hace ideal para transacciones frecuentes.',
        'icon' : 'fa-solid fa-wallet'
    },
    'Tarjeta de crédito': {
        'description' : 'Una tarjeta de crédito es una forma de financiamiento que permite a los usuarios realizar compras y pagarlas más tarde. Los usuarios pueden pagar el saldo en su totalidad cada mes o pueden optar por pagar un monto mínimo y pagar intereses sobre el saldo restante.',
        'icon' : 'fa-solid fa-credit-card'
    },
    'Activo': {
        'description' : 'Un activo es un recurso que posee una empresa o persona, como bienes raíces, inversiones o inventario. Los activos pueden ser tangibles o intangibles y se utilizan para generar ingresos.',
        'icon' : 'fa-solid fa-chart-line'
    },
    'Pasivo': {
        'description' : 'Un pasivo es una obligación financiera que tiene una empresa o persona, como préstamos, facturas pendientes o deudas. Los pasivos son una responsabilidad financiera y pueden afectar la capacidad de una empresa o persona para obtener financiamiento adicional o cumplir con sus obligaciones financieras existentes.',
        'icon' : 'fas fa-balance-scale-left'
    }
}


default_expense_categories = [
    {'name': 'Transporte', 'description': 'Gastos relacionados con el transporte', 'icon': 'fas fa-car'},
    {'name': 'Formación', 'description': 'Gastos relacionados con la educación y la formación', 'icon' : 'fas fa-graduation-cap'},
    {'name': 'Hogar', 'description': 'Gastos relacionados con el hogar y la decoración', 'icon' : 'fas fa-home'},
    {'name': 'Servicios públicos', 'description': 'Gastos relacionados con los servicios públicos como agua, luz, gas, etc.', 'icon' : 'fas fa-utensils'},
    {'name': 'Alimentos', 'description': 'Gastos relacionados con la compra de alimentos', 'icon' : 'fas fa-shopping-basket'},
    {'name': 'Suscripciones', 'description': 'Gastos relacionados con suscripciones a servicios y productos', 'icon' : 'fas fa-newspaper'},
    {'name': 'Vestimenta', 'description': 'Gastos relacionados con la ropa y la vestimenta', 'icon' : 'fas fa-tshirt'},
    {'name': 'Impuestos', 'description': 'Gastos relacionados con impuestos y tributos', 'icon' : 'fas fa-file-invoice-dollar'},
    {'name': 'Salud', 'description': 'Gastos relacionados con la salud y los cuidados médicos', 'icon': 'fas fa-medkit'},
    {'name': 'Entretenimiento', 'description': 'Gastos relacionados con el entretenimiento y los pasatiempos', 'icon': 'fas fa-gamepad'},
]