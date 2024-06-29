Feature: Voting Then Decision Making on Elucidat Learning Platform

  @kavin
  Scenario: Making a Case Against Kevin Then Voting
    Given I am on the Elucidat learning platform
    Then I verify the title is "Finding the Truth"
    Then I click on the START button
    Then I click on the Making a case against Kevin
    Then I click on JUDGE THIS button
    Then I click on Guilty Radio
    Then I click on Vote button
    Then I verify NOT GUILTY! headings on pop-up
    Then I click on the continue button on NOT GUILTY! pop-up
    Then I click on the continue button on EXPLORE THE EVIDENCE page
    Then I verify YOU DECIDE headings
    Then I click on continue button on YOU DECIDE page
    Then I click on flip button
    Then I click on Can be reliable radio button
    Then I click on Vote button again
    Then I verify Our expert agrees headings on pop-up
    Then I click on the continue button on Our expert agrees pop-up
