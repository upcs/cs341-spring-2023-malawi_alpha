<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Teacher View</title>
    <link rel="stylesheet" href="teacher-view.css" />
  </head>
  <?php include 'view-functionality' ?>
  <body>
    <form>
      <label for="class">Class</label>
      <select name="class" id="class">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
        <option value="11">11</option>
        <option value="12">12</option>
      </select>
      <label for="term">Term</label>
      <select name="term" id="term">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
      </select>
      <label for="year">Year</label>
      <select name="year" id="year">
        <option value="2021">2021</option>
        <option value="2022">2022</option>
        <option value="2023">2023</option>
        <option value="2024">2024</option>
        <option value="2025">2025</option>
        <option value="2026">2026</option>
        <option value="2027">2027</option>
        <option value="2028">2028</option>
        <option value="2029">2029</option>
        <option value="2030">2030</option>
      </select>
      <br /><br />
    </form>

    <div id="control-center">
      <textarea id="new-student" cols="30" rows="1"></textarea>
      <button type="submit" id="search-student-button">Search Student</button>

      <textarea id="token-text" cols="40" rows="1"></textarea>
      <button type="submit" id="token-button">Enter Token</button>

      <button type="submit" id="new-student-button">New Student</button>
      <button type="submit" id="printout-button">View Print Out</button>
    </div>

    <table width="100%" id="gradesheet">
      <tbody id="gradesheet-body">
        <tr>
          <td class="rotate-text">Class</td>
          <td class="rotate-text">Name</td>
          <td class="rotate-text">Position</td>
          <td class="rotate-text">Best of Five plus Eng</td>
          <td class="rotate-text">Running Average</td>
          <td class="rotate-text">POINTS</td>
          <td class="rotate-text">English</td>
          <td class="rotate-text">Physics</td>
          <td class="rotate-text">Chemistry</td>
          <td class="rotate-text">Biology</td>
          <td class="rotate-text">Maths</td>
          <td class="rotate-text">Social Studies</td>
          <td class="rotate-text">History</td>
          <td class="rotate-text">Geography</td>
          <td class="rotate-text">Agriculture</td>
          <td class="rotate-text">Bible Knowledge</td>
          <td class="rotate-text">Chichewa</td>
          <td class="rotate-text">French</td>
          <td class="rotate-text">Computer Studies</td>
          <td class="rotate-text">Life Skills</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
