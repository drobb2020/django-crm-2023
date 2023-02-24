console.log('Hello Django CRM World!')

// const btn = document.getElementById('alertbtn')
// const alert = document.getElementById('alert')

const alert_list = document.querySelectorAll('.alert')
alert_list.forEach(function (alert) {
  new bootstrap.Alert(alert)

  let alert_timeout = alert.getAttribute('data-timeout')
  setTimeout(() => {
    bootstrap.Alert.getInstance(alert).close()
  }, +alert_timeout)
})
