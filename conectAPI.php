<?php
$pergunta = $_POST["pergunta"];

if ($pergunta == "op1" || $pergunta == "op2" || $pergunta == "op3" || $pergunta == "op4"){
  $api_url = 'http://localhost:5000/DetalheResposta';


  $data = json_encode(['question' => $pergunta]);

  $ch = curl_init($api_url);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
  curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, True);
  curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-type: application/json',
    'Content-Length: ' . strlen($data)
  ]);

  $response = curl_exec($ch);
  curl_close($ch);

  $resultado = json_decode($response, true);
  $chatbot_resposta = $resultado['response'];



}else if ($pergunta == "op5" || $pergunta == "op6" || $pergunta == "op7"){
  $api_url = 'http://localhost:5000/ComoRecarregar';


  $data = json_encode(['question' => $pergunta]);

  $ch = curl_init($api_url);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
  curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, True);
  curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-type: application/json',
    'Content-Length: ' . strlen($data)
  ]);

  $response = curl_exec($ch);
  curl_close($ch);

  $resultado = json_decode($response, true);
  $chatbot_resposta = $resultado['response'];



}
else{

  $api_url = 'http://localhost:5000/chatBot';


  $data = json_encode(['question' => $pergunta]);

  $ch = curl_init($api_url);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
  curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, True);
  curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-type: application/json',
    'Content-Length: ' . strlen($data)
  ]);

  $response = curl_exec($ch);
  curl_close($ch);

  $resultado = json_decode($response, true);
  $chatbot_resposta = $resultado['response'];
}

echo json_encode($chatbot_resposta);

?>