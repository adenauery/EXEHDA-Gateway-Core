def css():
	return """
<style type= text/css>
  @media screen and (max-width: 600px) {
    u + .body {
      width: 100vw !important;
    }
  }
  a[x-apple-data-detectors] {
    color: inherit !important;
    text-decoration: none !important;
    font-size: inherit !important;
    font-family: inherit !important;
    font-weight: inherit !important;
    line-height: inherit !important;
  }
  body {
    margin: 0;
    padding: 0;
    background-color: #f5f7fb;
    font-size: 15px;
    line-height: 160%;
    mso-line-height-rule: exactly;
    color: #444;
    width: 100%;
  }
  @media only screen and (max-width: 560px) {
    body {
      font-size: 14px !important;
    }
  }
  body,
  table,
  td {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji",
      "Segoe UI Emoji", "Segoe UI Symbol";
  }
  table {
    border-collapse: collapse;
    width: 100%;
  }
  table:not(.main) {
    -premailer-cellpadding: 0;
    -premailer-cellspacing: 0;
  }
  .main {
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
  }
  .wrap {
    width: 100%;
    max-width: 640px;
    text-align: left;
  }
  .box {
    background: #fff;
    border-radius: 3px;
    -webkit-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
    border: 1px solid #f0f0f0;
  }
  .box + .box {
    margin-top: 24px;
  }
  .content {
    padding: 24px;
  }
  .h1,
  h1 {
    font-weight: 600;
    margin: 0 0 0.5em;
  }
  .h1 a,
  h1 a {
    color: inherit;
  }
  .h1,
  h1 {
    font-size: 28px;
    font-weight: 300;
    line-height: 130%;
  }
  @media only screen and (max-width: 560px) {
    .h1,
    h1 {
      font-size: 24px !important;
    }
  }
  img {
    border: 0 none;
    line-height: 100%;
    outline: 0;
    text-decoration: none;
    vertical-align: baseline;
    font-size: 0;
  }
  a {
    color: #467fcf;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  a img {
    border: 0 none;
  }
  strong {
    font-weight: 600;
  }
  .table td {
    padding: 4px 12px;
  }
  .table tr > td:first-child {
    padding-left: 0;
  }
  .table tr > td:last-child {
    padding-right: 0;
  }
  .btn {
    text-decoration: none;
    white-space: nowrap;
    font-weight: 600;
    font-size: 16px;
    padding: 12px 32px;
    border-radius: 3px;
    color: #fff;
    line-height: 100%;
    display: block;
    border: 1px solid transparent;
    -webkit-transition: 0.3s background-color;
    transition: 0.3s background-color;
  }
  .btn:hover {
    text-decoration: none;
  }
  .btn-span {
    color: #fff;
    font-size: 16px;
    text-decoration: none;
    white-space: nowrap;
    font-weight: 600;
    line-height: 100%;
  }
  .bg-body {
    background-color: #f5f7fb;
  }
  .text-muted {
    color: #9eb0b7;
  }
  .text-muted-light {
    color: #bbc8cd;
  }
  .bg-blue {
    background-color: #467fcf;
    color: #fff;
  }
  a.bg-blue:hover {
    background-color: #3a77cc !important;
  }
  .border-blue {
    border-color: #467fcf;
  }
  .text-right {
    text-align: right;
  }
  .text-center {
    text-align: center;
  }
  .va-middle {
    vertical-align: middle;
  }
  .img-illustration {
    max-width: 240px;
    max-height: 160px;
    width: auto;
    height: auto;
  }
  .rounded {
    border-radius: 3px;
  }
  table.rounded {
    border-collapse: separate;
  }
  .w-auto {
    width: auto;
  }
  .font-sm {
    font-size: 13px;
  }
  .lh-1 {
    line-height: 100%;
  }
  .border {
    border: 1px solid #f0f0f0;
  }
  .m-0 {
    margin: 0;
  }
  .pb-0 {
    padding-bottom: 0;
  }
  .p-sm {
    padding: 12px;
  }
  .pt-sm {
    padding-top: 8px;
  }
  .px-sm {
    padding-right: 8px;
  }
  .px-sm {
    padding-left: 8px;
  }
  .pt-md {
    padding-top: 16px;
  }
  .pb-md {
    padding-bottom: 16px;
  }
  .py-lg {
    padding-top: 24px;
  }
  .px-lg {
    padding-right: 24px;
  }
  .py-lg {
    padding-bottom: 24px;
  }
  .px-lg {
    padding-left: 24px;
  }
  .form-group {
    display: block;
  }
  .form-control {
    display: block;
    width: 100%;
    padding: 0.375rem 0.75rem;
    font-size: 0.9375rem;
    line-height: 1.6;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid rgba(0, 40, 100, 0.12);
    border-radius: 3px;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  }
  .form-label {
    display: block;
    margin-bottom: 0.375rem;
    font-weight: 600;
    font-size: 0.875rem;
  }

  .radio-p {
    display: flex;
    align-items: center;
  }
  .radio-p input{
    margin: 0 3px 0 0;
  }
  *, *::before, *::after {
    box-sizing: border-box;
  }
</style>
"""


def wifi_list(wifis):
	msg = ''
	for ssid, rssi, count in wifis:
		signal = ''
		if 0 > int(rssi) >= -50:
			signal = 'forte'
		elif -50 > int(rssi) >= -60:
			signal = 'médio'
		elif -60 > int(rssi) >= -70:
			signal = 'fraco'
		elif -70 > int(rssi):
			signal = 'ruim'

		msg += """
<p class="radio-p">
  <input type="radio" id="{ssid}" name="ssid" value="{count}">
  <label for="{ssid}">{ssid} (Sinal: {rssi})</label><br>
</p>
""".format(ssid=ssid, rssi=signal, count=count)
	return msg


def base(project, content):
	return """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta content="telephone=no" name="format-detection" />
    <title>{project}</title>
    {css}
  </head>
  <body class="bg-body">
    <center>
      <table class="main bg-body" width="100%" cellspacing="0" cellpadding="0">
        <tr>
          <td align="center" valign="top">
            <table class="wrap" cellspacing="0" cellpadding="0">
              <tr>
                <td class="p-sm">
                  <div class="main-content">
                    <table class="box" cellpadding="0" cellspacing="0">
                      <tr>
                        <td>
                          <table cellpadding="0" cellspacing="0">
                            <tr>
                              <td class="content pb-0" align="left">
                                <h2 class="m-0">
                                  <strong>{project}</strong>
                                  <br />
                                  <strong>Configuração de Wi-Fi do Gateway</strong>
                                </h2>
                              </td>
                            </tr>
                            <tr>
                              {content}
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                  <table cellspacing="0" cellpadding="0">
                    <tr>
                      <td class="py-lg">
                        <table
                          class="font-sm text-center text-muted"
                          cellspacing="0"
                          cellpadding="0"
                        >
                          <tr>
                            <td class="px-lg">
                              Em caso de dúvidas, entre em contato com os representantes do projeto.
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </center>
  </body>
</html>
""".format(css=css(), project=project, content=content)


def main(project, wifis):
	msg = """
<td class="content pt-sm">
  <form action="configure" method="post">
    <br />
    <strong>
      Selecione uma rede Wi-Fi e insira a senha para configurar este dispositivo.
    </strong>
    <br />
    {wifi_list}
    <p>
      <div class="form-group">
        <label class="form-label">Senha</label>
        <input name="password" type="password" class="form-control">
      </div>
    </p>
    <table
      cellpadding="0"
      cellspacing="0"
      class="bg-blue rounded w-auto"
    >
      <tr>
        <td valign="top" class="lh-1">
          <button
            type="submit" 
            class="btn bg-blue border-blue"
          >
            <span class="btn-span">
              Avançar
            </span>
          </button>
        </td>
      </tr>
    </table>
  </form>
</td>
""".format(wifi_list=wifi_list(wifis))
	return base(project, msg)


def success(project, ssid):
	msg = """
<td class="content pt-sm">
  <br />
  <p>
    O gateway se conectou com sucesso a rede Wi-Fi <strong>{ssid}</strong> e estará disponível para uso em instantes.
  </p>
</td>
""".format(ssid=ssid)
	return base(project, msg)


def base_error(message):
	msg = """
<td class="content pt-sm">
	<br />
	<p>
		{message}
	</p>
	<table
		cellpadding="0"
		cellspacing="0"
		class="bg-blue rounded w-auto"
	>
		<tr>
			<td valign="top" class="lh-1">
				<a
					href="/"
					class="btn bg-blue border-blue"
				>
					<span class="btn-span">Voltar</span>
				</a>
			</td>
		</tr>
	</table>
</td>
""".format(message=message)
	return msg


def failure(project, ssid):
	return base(project, base_error("Não foi possivel conectar a rede Wi-Fi <strong>{ssid}</strong>. Por favor, verifique os campos e tente novamente.".format(ssid=ssid)))


def parameter_not_found(project):
	return base(project, base_error("Não foram selecionados parametros para configuração. Por favor, tente novamente."))


def ssid_not_found(project):
	return base(project, base_error("Selecione uma rede para concluir a configuração deste dispositivo."))


def not_found(project):
	return base(project, base_error("Desculpe, esta página não está disponível. O endereço que você acessou parece estar quebrado ou a página que você acessou não existe."))
