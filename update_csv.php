<?php
header('Content-Type: application/json');

$data = json_decode(file_get_contents('php://input'), true);

$csvFile = 'conversation_choices.csv';
$csvData = array_map('str_getcsv', file($csvFile));

$headers = $csvData[0];
$counts = array_map('intval', $csvData[1]);

foreach ($data as $selection) {
    $answer = $selection['answer'];
    $index = array_search($answer, $headers);
    if ($index !== false) {
        $counts[$index]++;
    }
}

$fp = fopen($csvFile, 'w');
fputcsv($fp, $headers);
fputcsv($fp, $counts);
fclose($fp);

echo json_encode(['success' => true]);