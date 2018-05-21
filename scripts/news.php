<p class="bigger">DN.se - Senaste nytt</p> <br />
<?php
  header("Content-Type: text/html");
  $rss = new DOMDocument();
  $rss->load('http://dn.se/rss/senaste-nytt');
  $feed = array();
    foreach ($rss->getElementsByTagName('item') as $node) {
      $item = array (
      'title' => $node->getElementsByTagName('title')->item(0)->nodeValue,
      'desc' => $node->getElementsByTagName('description')->item(0)->nodeValue,
      'date' => $node->getElementsByTagName('pubDate')->item(0)->nodeValue,
      );
    array_push($feed, $item);
    }

  $limit = 2; // Number of posts to be displayed
  for($x=0;$x<$limit;$x++) {
    $title = str_replace(' & ', ' &amp; ', $feed[$x]['title']);
    $description = $feed[$x]['desc'];
    $date = date('j F', strtotime($feed[$x]['date']));
    echo '<h2 class="smaller">'.$title.'</h2>';
    echo '<p>'.strip_tags($description, '<p><b>').'</p><h2><br /></h2>';
  }
?>
