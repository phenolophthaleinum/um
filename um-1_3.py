import regex as re

#text = input("your text:")

# example site
text = '''






<!DOCTYPE html>
<html lang="en" data-color-mode="dark" data-light-theme="light" data-dark-theme="dark">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">



  <link crossorigin="anonymous" media="all" integrity="sha512-BEwN74xxmv+L2zArQGm+kGVvX3bGY85LF4umkZnZ6Zl6IciYbr1IGxIYxqnUCW0RDEN1kM7glvXkpmQsntPVYQ==" rel="stylesheet" href="https://github.githubassets.com/assets/dark-044c0def8c719aff8bdb.css" /><link data-color-theme="light" crossorigin="anonymous" media="all" integrity="sha512-9M4GwJqBATCm6CMz2UrCo6uuX1/Wa8wUnm7N5BQhGHFch1oIX2y8dcpUXfnQVQ2HE2bD287O5YMXuc5jFAcU8w==" rel="stylesheet" data-href="https://github.githubassets.com/assets/light-f4ce06c09a810130a6e8.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" integrity="sha512-VuoBmyfgmCH9NsX74/R66RxQGfjoTNNTUdFUi9HeWSwDRckcVZHH1xn6VwcMa08p8xSCO2udmiuA12lR9TAzxA==" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-56ea019b27e09821fd36.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" integrity="sha512-jHPIsHz149JE+ZbsS8f5oQFqdU/HHlWk8+AnPsA0+zZaVQkSidWMmCiT/DCiLLn6uAXgdnXxFr1GG1SWrBnnUQ==" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-8c73c8b07cf5e3d244f9.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" integrity="sha512-7p7WmGYFN2EAFuK148e628pqxO+aqNIa7ik/Y38lMirTnrxjHqBKXYBOaCxBjmz2r60YWkzb+TqMR8CjeqAUNQ==" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-ee9ed698660537610016.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" integrity="sha512-vFYO2hdW9+5z6u5jCkMIIcslIZGySqnMAzuYZEXT2FyJjx9f8A6rtAMdYn4nVSXOe1TIhT/UCWYgnszpePyMVA==" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-bc560eda1756f7ee73ea.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" integrity="sha512-uaQhAu1uyRSlhFCuVq+c2TI/raBoawOri5enqBMFrNvRVOop44KjS/gnsHEHmzh/HrI2MrwXOLLuQouKPzce3A==" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-b9a42102ed6ec914a584.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-QDstDV0CeaTAQxEaLoguDaXfF719UOKQClVxrV8b6QIqX5ofij6Hzazl5koLCQdlPoVkHQP46nq7tmwJsixVaA==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-403b2d0d5d0279a4c043.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-5ISNWkOjNGh9+d5QNsfYbBC62GLVhSrLzdT68QtA+uGXsnvMWzzKBEmwzSpSbkNsl52ks1Ts8nButa1+XGu7oQ==" rel="stylesheet" href="https://github.githubassets.com/assets/behaviors-e4848d5a43a334687df9.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-hpIrfz2pWwa7eGZ5dC5vHGZ25lJj1iVSVx6xl6yyaGBCYJ5jsX2myq3ToniMuK4eHVL6iw/fKHj++Cg/hdB0JA==" rel="stylesheet" href="https://github.githubassets.com/assets/tab-size-fix-86922b7f3da95b06bb78.css" />
  
  
  
  <link crossorigin="anonymous" media="all" integrity="sha512-1nwP7mOTtxd5kt7EmBrhD1q0R7VXGymiuBEZofVjFBe6RwKT92Paw+dqHRz2qFJjvAOsrJWVIWw0wQHOEEqcGw==" rel="stylesheet" href="https://github.githubassets.com/assets/github-d67c0fee6393b7177992.css" />

    <meta name="optimizely-datafile" content="{&quot;version&quot;: &quot;4&quot;, &quot;rollouts&quot;: [], &quot;typedAudiences&quot;: [], &quot;anonymizeIP&quot;: true, &quot;projectId&quot;: &quot;16737760170&quot;, &quot;variables&quot;: [], &quot;featureFlags&quot;: [], &quot;experiments&quot;: [{&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20438636352&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20484957397&quot;, &quot;key&quot;: &quot;treatment&quot;}], &quot;id&quot;: &quot;20479227424&quot;, &quot;key&quot;: &quot;growth_ghec_onboarding_experience&quot;, &quot;layerId&quot;: &quot;20467848595&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20484957397&quot;, &quot;endOfRange&quot;: 1000}, {&quot;entityId&quot;: &quot;20484957397&quot;, &quot;endOfRange&quot;: 3000}, {&quot;entityId&quot;: &quot;20484957397&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20484957397&quot;, &quot;endOfRange&quot;: 6000}, {&quot;entityId&quot;: &quot;20484957397&quot;, &quot;endOfRange&quot;: 8000}, {&quot;entityId&quot;: &quot;20484957397&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;85e2238ce2b9074907d7a3d91d6feeae&quot;: &quot;control&quot;}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20667381018&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20680930759&quot;, &quot;key&quot;: &quot;treatment&quot;}], &quot;id&quot;: &quot;20652570897&quot;, &quot;key&quot;: &quot;project_genesis&quot;, &quot;layerId&quot;: &quot;20672300363&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20667381018&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20680930759&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {&quot;83356e17066d336d1803024138ecb683&quot;: &quot;treatment&quot;, &quot;18e31c8a9b2271332466133162a4aa0d&quot;: &quot;treatment&quot;, &quot;10f8ab3fbc5ebe989a36a05f79d48f32&quot;: &quot;treatment&quot;, &quot;1686089f6d540cd2deeaec60ee43ecf7&quot;: &quot;treatment&quot;}}, {&quot;status&quot;: &quot;Running&quot;, &quot;audienceIds&quot;: [], &quot;variations&quot;: [{&quot;variables&quot;: [], &quot;id&quot;: &quot;20898546114&quot;, &quot;key&quot;: &quot;control&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20923036705&quot;, &quot;key&quot;: &quot;treatment_a&quot;}, {&quot;variables&quot;: [], &quot;id&quot;: &quot;20965581308&quot;, &quot;key&quot;: &quot;treatment_b&quot;}], &quot;id&quot;: &quot;20902325119&quot;, &quot;key&quot;: &quot;contact_sales_page_optimizations&quot;, &quot;layerId&quot;: &quot;20969031091&quot;, &quot;trafficAllocation&quot;: [{&quot;entityId&quot;: &quot;20965581308&quot;, &quot;endOfRange&quot;: 3330}, {&quot;entityId&quot;: &quot;20898546114&quot;, &quot;endOfRange&quot;: 5000}, {&quot;entityId&quot;: &quot;20898546114&quot;, &quot;endOfRange&quot;: 6670}, {&quot;entityId&quot;: &quot;20923036705&quot;, &quot;endOfRange&quot;: 10000}], &quot;forcedVariations&quot;: {}}], &quot;audiences&quot;: [{&quot;conditions&quot;: &quot;[\&quot;or\&quot;, {\&quot;match\&quot;: \&quot;exact\&quot;, \&quot;name\&quot;: \&quot;$opt_dummy_attribute\&quot;, \&quot;type\&quot;: \&quot;custom_attribute\&quot;, \&quot;value\&quot;: \&quot;$opt_dummy_value\&quot;}]&quot;, &quot;id&quot;: &quot;$opt_dummy_audience&quot;, &quot;name&quot;: &quot;Optimizely-Generated Audience for Backwards Compatibility&quot;}], &quot;groups&quot;: [], &quot;sdkKey&quot;: &quot;WTc6awnGuYDdG98CYRban&quot;, &quot;environmentKey&quot;: &quot;production&quot;, &quot;attributes&quot;: [{&quot;id&quot;: &quot;16822470375&quot;, &quot;key&quot;: &quot;user_id&quot;}, {&quot;id&quot;: &quot;17143601254&quot;, &quot;key&quot;: &quot;spammy&quot;}, {&quot;id&quot;: &quot;18175660309&quot;, &quot;key&quot;: &quot;organization_plan&quot;}, {&quot;id&quot;: &quot;18813001570&quot;, &quot;key&quot;: &quot;is_logged_in&quot;}, {&quot;id&quot;: &quot;19073851829&quot;, &quot;key&quot;: &quot;geo&quot;}, {&quot;id&quot;: &quot;20175462351&quot;, &quot;key&quot;: &quot;requestedCurrency&quot;}, {&quot;id&quot;: &quot;20785470195&quot;, &quot;key&quot;: &quot;country_code&quot;}], &quot;botFiltering&quot;: false, &quot;accountId&quot;: &quot;16737760170&quot;, &quot;events&quot;: [{&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;17911811441&quot;, &quot;key&quot;: &quot;hydro_click.dashboard.teacher_toolbox_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18124116703&quot;, &quot;key&quot;: &quot;submit.organizations.complete_sign_up&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18145892387&quot;, &quot;key&quot;: &quot;no_metric.tracked_outside_of_optimizely&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18178755568&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.add_repo&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18180553241&quot;, &quot;key&quot;: &quot;submit.repository_imports.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18186103728&quot;, &quot;key&quot;: &quot;click.help.learn_more_about_repository_creation&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18188530140&quot;, &quot;key&quot;: &quot;test_event&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18191963644&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.transfer_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18195612788&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.import_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18210945499&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.invite_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18211063248&quot;, &quot;key&quot;: &quot;click.empty_org_repo_cta.create_repository&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18215721889&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.update_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18224360785&quot;, &quot;key&quot;: &quot;click.org_onboarding_checklist.dismiss&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18234832286&quot;, &quot;key&quot;: &quot;submit.organization_activation.complete&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18252392383&quot;, &quot;key&quot;: &quot;submit.org_repository.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18257551537&quot;, &quot;key&quot;: &quot;submit.org_member_invitation.create&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18259522260&quot;, &quot;key&quot;: &quot;submit.organization_profile.update&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18564603625&quot;, &quot;key&quot;: &quot;view.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18568612016&quot;, &quot;key&quot;: &quot;click.classroom_sign_in_click&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18572592540&quot;, &quot;key&quot;: &quot;view.classroom_name&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18574203855&quot;, &quot;key&quot;: &quot;click.classroom_create_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18582053415&quot;, &quot;key&quot;: &quot;click.classroom_select_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18589463420&quot;, &quot;key&quot;: &quot;click.classroom_create_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591323364&quot;, &quot;key&quot;: &quot;click.classroom_create_first_classroom&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18591652321&quot;, &quot;key&quot;: &quot;click.classroom_grant_access&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;18607131425&quot;, &quot;key&quot;: &quot;view.classroom_creation&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;18831680583&quot;, &quot;key&quot;: &quot;upgrade_account_plan&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19064064515&quot;, &quot;key&quot;: &quot;click.signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19075373687&quot;, &quot;key&quot;: &quot;click.view_account_billing_page&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19077355841&quot;, &quot;key&quot;: &quot;click.dismiss_signup_prompt&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19079713938&quot;, &quot;key&quot;: &quot;click.contact_sales&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19120963070&quot;, &quot;key&quot;: &quot;click.compare_account_plans&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19151690317&quot;, &quot;key&quot;: &quot;click.upgrade_account_cta&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19424193129&quot;, &quot;key&quot;: &quot;click.open_account_switcher&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19520330825&quot;, &quot;key&quot;: &quot;click.visit_account_profile&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19540970635&quot;, &quot;key&quot;: &quot;click.switch_account_context&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19730198868&quot;, &quot;key&quot;: &quot;submit.homepage_signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19820830627&quot;, &quot;key&quot;: &quot;click.homepage_signup&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;19988571001&quot;, &quot;key&quot;: &quot;click.create_enterprise_trial&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20036538294&quot;, &quot;key&quot;: &quot;click.create_organization_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20040653299&quot;, &quot;key&quot;: &quot;click.input_enterprise_trial_form&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20062030003&quot;, &quot;key&quot;: &quot;click.continue_with_team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20068947153&quot;, &quot;key&quot;: &quot;click.create_organization_free&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20086636658&quot;, &quot;key&quot;: &quot;click.signup_continue.username&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20091648988&quot;, &quot;key&quot;: &quot;click.signup_continue.create_account&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20103637615&quot;, &quot;key&quot;: &quot;click.signup_continue.email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20111574253&quot;, &quot;key&quot;: &quot;click.signup_continue.password&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20120044111&quot;, &quot;key&quot;: &quot;view.pricing_page&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20152062109&quot;, &quot;key&quot;: &quot;submit.create_account&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20165800992&quot;, &quot;key&quot;: &quot;submit.upgrade_payment_form&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20171520319&quot;, &quot;key&quot;: &quot;submit.create_organization&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20222645674&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.discuss_your_needs&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20227443657&quot;, &quot;key&quot;: &quot;submit.verify_primary_user_email&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20234607160&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.try_enterprise&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20238175784&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.team&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20239847212&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.continue_free&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20251097193&quot;, &quot;key&quot;: &quot;recommended_plan&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20438619534&quot;, &quot;key&quot;: &quot;click.pricing_calculator.1_member&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20456699683&quot;, &quot;key&quot;: &quot;click.pricing_calculator.15_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20467868331&quot;, &quot;key&quot;: &quot;click.pricing_calculator.10_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20476267432&quot;, &quot;key&quot;: &quot;click.trial_days_remaining&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20476357660&quot;, &quot;key&quot;: &quot;click.discover_feature&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20479287901&quot;, &quot;key&quot;: &quot;click.pricing_calculator.custom_members&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20481107083&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.apply_teacher_benefits&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20483089392&quot;, &quot;key&quot;: &quot;click.pricing_calculator.5_members&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;, &quot;20652570897&quot;], &quot;id&quot;: &quot;20484283944&quot;, &quot;key&quot;: &quot;click.onboarding_task&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20484996281&quot;, &quot;key&quot;: &quot;click.recommended_plan_in_signup.apply_student_benefits&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20486713726&quot;, &quot;key&quot;: &quot;click.onboarding_task_breadcrumb&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20490791319&quot;, &quot;key&quot;: &quot;click.upgrade_to_enterprise&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20491786766&quot;, &quot;key&quot;: &quot;click.talk_to_us&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20494144087&quot;, &quot;key&quot;: &quot;click.dismiss_enterprise_trial&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;, &quot;20652570897&quot;], &quot;id&quot;: &quot;20499722759&quot;, &quot;key&quot;: &quot;completed_all_tasks&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;, &quot;20652570897&quot;], &quot;id&quot;: &quot;20500710104&quot;, &quot;key&quot;: &quot;completed_onboarding_tasks&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20513160672&quot;, &quot;key&quot;: &quot;click.read_doc&quot;}, {&quot;experimentIds&quot;: [&quot;20652570897&quot;], &quot;id&quot;: &quot;20516196762&quot;, &quot;key&quot;: &quot;actions_enabled&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20518980986&quot;, &quot;key&quot;: &quot;click.dismiss_trial_banner&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20535446721&quot;, &quot;key&quot;: &quot;click.issue_actions_prompt.dismiss_prompt&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20557002247&quot;, &quot;key&quot;: &quot;click.issue_actions_prompt.setup_workflow&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20595070227&quot;, &quot;key&quot;: &quot;click.pull_request_setup_workflow&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20626600314&quot;, &quot;key&quot;: &quot;click.seats_input&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20642310305&quot;, &quot;key&quot;: &quot;click.decrease_seats_number&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20662990045&quot;, &quot;key&quot;: &quot;click.increase_seats_number&quot;}, {&quot;experimentIds&quot;: [], &quot;id&quot;: &quot;20679620969&quot;, &quot;key&quot;: &quot;click.public_product_roadmap&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20761240940&quot;, &quot;key&quot;: &quot;click.dismiss_survey_banner&quot;}, {&quot;experimentIds&quot;: [&quot;20479227424&quot;], &quot;id&quot;: &quot;20767210721&quot;, &quot;key&quot;: &quot;click.take_survey&quot;}, {&quot;experimentIds&quot;: [&quot;20652570897&quot;], &quot;id&quot;: &quot;20795281201&quot;, &quot;key&quot;: &quot;click.archive_list&quot;}, {&quot;experimentIds&quot;: [&quot;20902325119&quot;], &quot;id&quot;: &quot;20966790249&quot;, &quot;key&quot;: &quot;contact_sales.submit&quot;}, {&quot;experimentIds&quot;: [&quot;20902325119&quot;], &quot;id&quot;: &quot;20996500333&quot;, &quot;key&quot;: &quot;contact_sales.existing_customer&quot;}, {&quot;experimentIds&quot;: [&quot;20902325119&quot;], &quot;id&quot;: &quot;20996890162&quot;, &quot;key&quot;: &quot;contact_sales.blank_message_field&quot;}, {&quot;experimentIds&quot;: [&quot;20902325119&quot;], &quot;id&quot;: &quot;21000470317&quot;, &quot;key&quot;: &quot;contact_sales.personal_email&quot;}, {&quot;experimentIds&quot;: [&quot;20902325119&quot;], &quot;id&quot;: &quot;21002790172&quot;, &quot;key&quot;: &quot;contact_sales.blank_phone_field&quot;}], &quot;revision&quot;: &quot;1065&quot;}" />


  <script crossorigin="anonymous" defer="defer" integrity="sha512-42SXFvQHDz2FyN94xIyfcefqRg+Rr0oaj8QR12wnRhCuREAcqJa251RtFwUdt6YhydPAqg+H7POP4+ggIjWrFQ==" type="application/javascript" src="https://github.githubassets.com/assets/environment-e3649716.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-5CoW/JieJEi1EVuAsF/qwHehVAAKL99wx4omWKPGZ+EpB+QbnkbLHoUwcIxZ0WyKPH0jxH/DT/X457bllH6zGg==" type="application/javascript" src="https://github.githubassets.com/assets/chunk-frameworks-e42a16fc.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-CTwG9GT4xr4Vb2vCWNfDojO0Iqz90nxevV5Ar5Mozo5gneSOU1cDZ402ond5RAsUzdTqzQDsCnOE284z4FdrEQ==" type="application/javascript" src="https://github.githubassets.com/assets/chunk-vendor-093c06f4.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-vgWV8b1FcpGErHwOitpIbvNmtQZwsw55TUraZngdfnHB3P+ZQnxzKD1L//RqzlWMB9sExBRhfOt1rHCxrru/Fg==" type="application/javascript" src="https://github.githubassets.com/assets/github-elements-be0595f1.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-NrzAYwNX19WW2mDsthNaaMhLn1yzmeMxRuB+OrqcFjWGjkV81E4txVViMRpiNXho430qH302NtjQI24XVIo0FQ==" type="application/javascript" src="https://github.githubassets.com/assets/element-registry-36bcc063.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-W9agUalssdu+Q3uNJwESWikQLPZXC/Ut8qceEthickNKNIAPhC2ARBWCg6nX7H1rrOiKyDVCPUgSAtB9p5zybA==" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-5bd6a051.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-QJOVXs8UW2egqYjA0sv3TAATdCX6IAdBOGd8ScZJVfP1WJAWg6nh/P8FUKERkAjIviTKAMUwh9OEnbtnTz8PKw==" type="application/javascript" src="https://github.githubassets.com/assets/notifications-global-4093955e.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-0AWnITMRwpt2M7zejhGSMZMWcEBeswVLaglGmkxpQOWEnhnJpAGMuZ0iOLIKJzpuYP2xuNZK51OMM0e5TRUkAA==" type="application/javascript" data-module-id="./chunk-action-list-element.js" data-src="https://github.githubassets.com/assets/chunk-action-list-element-d005a721.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-vu177vjMAp7fHx+zkCoAvGVkQPtNX1L2oWm3v4J1k6WbHtUI8iQMc8ovtNOKnN89/npQsJrksRBjWyJauDJuaw==" type="application/javascript" data-module-id="./chunk-advanced.js" data-src="https://github.githubassets.com/assets/chunk-advanced-beed7bee.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-iG8aKaXiAy7ONu7OJuY1pf3FGFzrs4mYYGnUD47a1kXP5URyMlP1RpAFyWTFeyirHY/UoR2mmkkBD40j/9ouPA==" type="application/javascript" data-module-id="./chunk-animate-on-scroll.js" data-src="https://github.githubassets.com/assets/chunk-animate-on-scroll-886f1a29.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-DR/O+c2yX9jstdyxwVDlaM8zRuOACj/aap9ABecyw8toE3a9rXjQgytQlFPQu74JufIDXrD3E1xAOX+ZscWG1g==" type="application/javascript" data-module-id="./chunk-area.js" data-src="https://github.githubassets.com/assets/chunk-area-0d1fcef9.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-lchWLejOHZUQUJA5VcNlSnbRzzpiJVi0Sg1NcZTkhocfF0PDO8LeAkitCPsqUWW6F2hznj3bDp2rouTLXug6/Q==" type="application/javascript" data-module-id="./chunk-array.js" data-src="https://github.githubassets.com/assets/chunk-array-95c8562d.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-owLCfEz1kyCuCC2dJj3PrIlbMLSAatThR4RbMUlvOdTBRzOf7bjbnY+5VhhGyLMO+M9LxaITgDkHkZjQ+Vzvng==" type="application/javascript" data-module-id="./chunk-axis.js" data-src="https://github.githubassets.com/assets/chunk-axis-a302c27c.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-m/O2Z0gPqnm57wbjLsBOvQh6Q2Pe9ZPuJB//JVxnLopUDBm+2oIbe85Dtn7Gxa3vxLD0dnPsyzLnZ1p2rnMsMQ==" type="application/javascript" data-module-id="./chunk-band.js" data-src="https://github.githubassets.com/assets/chunk-band-9bf3b667.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-eGxp1b7dZ1/tJRddGRSK4XEFLlUWaApzGS/WiLLNaH03D5ZEOsf0pozYT2DfAGxsar1XKqw16YJ/Zdqrl3W94g==" type="application/javascript" data-module-id="./chunk-bar-chart.js" data-src="https://github.githubassets.com/assets/chunk-bar-chart-786c69d5.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-1sfVVMUvgk/el5qm4XY7G3N6Ayu9Rob6D3L4SLwpQ7YRagyYcPbOwz0I6pekJeYdm4qCWJ7r5Gjxv7aMFahFyg==" type="application/javascript" data-module-id="./chunk-branch-from-issue-button.js" data-src="https://github.githubassets.com/assets/chunk-branch-from-issue-button-d6c7d554.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-Qmuvn45kThf+SjmbdA0SjW/zOXYKhhnCWwe3kUNKqyEMtxh7k+sZTXTvMR/DCekAWpyv2P1hCrY9SOK0GpWCLA==" type="application/javascript" data-module-id="./chunk-business-audit-log-map-element.js" data-src="https://github.githubassets.com/assets/chunk-business-audit-log-map-element-426baf9f.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-wuxyUzhHyxJAliatPrzLlF9/JXffBvm8VcGEqLamI2l0k1SegKEbJTU3Ho8fC8uuwjKD3nF5v9q3nlnxgFrJVw==" type="application/javascript" data-module-id="./chunk-code-frequency-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-code-frequency-graph-element-c2ec7253.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-/pLSBAJaIyy02rB8GR0Ca3InIc+gQwIBKsnxSdPfuKvC2kELy5s5QpoNQjJvILONrZeYECH9OLjTp+I65P0h0g==" type="application/javascript" data-module-id="./chunk-codemirror-linter-util.js" data-src="https://github.githubassets.com/assets/chunk-codemirror-linter-util-fe92d204.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-ep6n62OPA1P1ThFWfIZLLymoFA20VFe9/FxtagWNtucAgqTk6r2EdaNqJsM60bJvu9c+qxJ3IemOHRCZKxoc8Q==" type="application/javascript" data-module-id="./chunk-codemirror.js" data-src="https://github.githubassets.com/assets/chunk-codemirror-7a9ea7eb.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-J8jHMgG3jS4CpHyg8r7/4fkGdTqIN02DLHqUXcqIAmRWCEgjN1dBjBocAjsdSxTK9aSuLAcdk+BxOsvXA/XbyA==" type="application/javascript" data-module-id="./chunk-codespaces-policy-form-element.js" data-src="https://github.githubassets.com/assets/chunk-codespaces-policy-form-element-27c8c732.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-xhSAO0KtnFAlRqAK+mg8BPj/J334ccvnCmmjmBQBCgZcsoO9teHJSS6oAn3XOWYFsWPU2JehwG7S3OVEbLwdUg==" type="application/javascript" data-module-id="./chunk-color-modes.js" data-src="https://github.githubassets.com/assets/chunk-color-modes-c614803b.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-v8cHj6fIJrUr2THCh/9KFMq1ynoKuurR4+FC2Ett8SMLXKeZlPKNBdug2YUHDTdReeN3k8V4w5alEdiPSoSaZw==" type="application/javascript" data-module-id="./chunk-column-chart.js" data-src="https://github.githubassets.com/assets/chunk-column-chart-bfc7078f.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-e2tAI38b5I3l97moOEkqs9yFffRHHR+P32shCGZ+n62mdjAkXN8hyP1itzlxIFLqaGZqbJ+gthhrE88opzmQ+A==" type="application/javascript" data-module-id="./chunk-command-palette-item-element.js" data-src="https://github.githubassets.com/assets/chunk-command-palette-item-element-7b6b4023.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-Hy/BNedLOb00IX7wv9xbIJ0pZsLuwvNsSjgpNIaz/9eo/iUKfPMtQL19gxTWpz6nZ43QLfYYIy4QoL7oBUmgww==" type="application/javascript" data-module-id="./chunk-command-palette-page-element.js" data-src="https://github.githubassets.com/assets/chunk-command-palette-page-element-1f2fc135.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-v9LXKvRELqsowcou8tLTR6l5xTTGdvCuGAJkJwxGvev1tPItmj5dvqgev9P+49KwCo3AU1VRYJsQbTVaMtDpag==" type="application/javascript" data-module-id="./chunk-command-palette-page-stack-element.js" data-src="https://github.githubassets.com/assets/chunk-command-palette-page-stack-element-bfd2d72a.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-ZYjZKQHIOhwDjM01xaTY5HVOYxow2dSPnRUCCysGwB/MggQEIZDqUBLSJH3+UfOVcLld2RcFA7vfjkinMQimSg==" type="application/javascript" data-module-id="./chunk-commit-activity-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-commit-activity-graph-element-6588d929.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-wjhbw7qkjmwL4LD+tmeYjd+1ABG7/xOknSlnwKAOz9cfRwhihOaEfiTWJ85/7slhTYZqECBzLbKVqZKQastHIw==" type="application/javascript" data-module-id="./chunk-community-contributions.js" data-src="https://github.githubassets.com/assets/chunk-community-contributions-c2385bc3.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-HDsLJf6gAN+WDFaJneJwmIY82XkZKWqeX7tStBLRh1XM53K8vMV6JZvjq/UQXszaNVWxWcuYtgYTG6ZWo8+QSw==" type="application/javascript" data-module-id="./chunk-confetti.js" data-src="https://github.githubassets.com/assets/chunk-confetti-1c3b0b25.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-wpenTjQMyR7zUKeyNv37Agdwcr3a/c71kpUwVTrExMbL6RFpA/g8aL+I5AbLKuaw4dyVjNfy0DFHBmFqm8Yr+A==" type="application/javascript" data-module-id="./chunk-contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/chunk-contributions-spider-graph-c297a74e.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-IpKybX6qZXRhU3S4Isw2/xiKMrWBFURLL87mlSWRbqdyOuVLuLfj7AvGOzJlfhtbMDk3uG+VZTpD01TaH6Ph/w==" type="application/javascript" data-module-id="./chunk-contributors-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-contributors-graph-element-2292b26d.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-AdShwMIaVrtYr+LC9cc7rsC64wQJgoCdDjLJXaD4kVhdmuld7dk748AQueuoomE4OZypdoHSPmxQ56Wge/qtig==" type="application/javascript" data-module-id="./chunk-cookies.js" data-src="https://github.githubassets.com/assets/chunk-cookies-01d4a1c0.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-jitxouuFY6SUcDZV5W3jhadVEIfFBfCQZxfPV3kxNnsWEBzbxMJFp0ccLb7+OlBjSs1zU/MNtuOV6T9Ay7lx4w==" type="application/javascript" data-module-id="./chunk-copy.js" data-src="https://github.githubassets.com/assets/chunk-copy-8e2b71a2.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-miaiZ1xkDsWBUsURHOmeYtbgVKQGnm1octCo/lDXUmPzDyjtubnHULRVw1AK+sttwdwyB0+LOyhIVAWCNSGx+A==" type="application/javascript" data-module-id="./chunk-delayed-loading-element.js" data-src="https://github.githubassets.com/assets/chunk-delayed-loading-element-9a26a267.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-g9egUfzV36Fhfld8PbxfEm/V9ePFqvd9i5DIKra4wJ61M/AnpOOadhUD2CZ//ww84eRnAMJRQRHOYZ2wZRo2IQ==" type="application/javascript" data-module-id="./chunk-dependencies.js" data-src="https://github.githubassets.com/assets/chunk-dependencies-83d7a051.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-LlVyc/1U000RmO4RldBXJllTDjCahXcYhoH36e/5Z7FQrfr76hILqzCSPa7I0Jq0dXrUmF7Rdlgr8upKiqI4bQ==" type="application/javascript" data-module-id="./chunk-discussion-page-views.js" data-src="https://github.githubassets.com/assets/chunk-discussion-page-views-2e557273.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-VZ4h8Fwcm0XTbcjGFRmk/9GAADXVkklCPuqF5hBT2HVzegZMZD4SRS89VErsHdrBhD+BVvpsEEJ5fislbVANsw==" type="application/javascript" data-module-id="./chunk-discussions-daily-contributors.js" data-src="https://github.githubassets.com/assets/chunk-discussions-daily-contributors-559e21f0.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-UTkDkF19l+4mKyXJ7GhLKMFoVgExzifWypg7Fv+ymgs5p7tKNt/owkzPouakQub6lkkp0nhd8wE6rGf3UwUZqg==" type="application/javascript" data-module-id="./chunk-discussions-new-contributors.js" data-src="https://github.githubassets.com/assets/chunk-discussions-new-contributors-51390390.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-W2h1jdFgngGW5/6LmW+E+jNqLFqt8UGenaQj7UWfK0CqdQjahNQXW6OuZlzkQcthIZ8V8AZpZDolxoQ8Kd3Gaw==" type="application/javascript" data-module-id="./chunk-dormant-users-reports.js" data-src="https://github.githubassets.com/assets/chunk-dormant-users-reports-5b68758d.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-T092OZtYeslxDIimT2TR4IWlO+6B9q6zenOAqRekKME3TgdR1nKinRgV0PTYZ3Y3IITjimtvjqQpN5kW11o0bw==" type="application/javascript" data-module-id="./chunk-drag-drop.js" data-src="https://github.githubassets.com/assets/chunk-drag-drop-4f4f7639.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-nqSGfQ+YUbpCws7n/18G/ueeeWfuJYlTMaRBOIPUGh2NOPEUQm4YW7NjctpPQgAWoVIaeEr0XDFXCWBbFW9sXQ==" type="application/javascript" data-module-id="./chunk-edit-hook-secret-element.js" data-src="https://github.githubassets.com/assets/chunk-edit-hook-secret-element-9ea4867d.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-lJhSlHBxDYfafMGsvjfmbReBxHE64RGTSucXtcG3vTpWvu2vlw/heQjiHB+JwYpnWvcXh0Tn9oLlo90LEpUfIA==" type="application/javascript" data-module-id="./chunk-edit.js" data-src="https://github.githubassets.com/assets/chunk-edit-94985294.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-lZ+KI9egKP++FYD5qpzdWdu26uB+Hi81g+o1fapRMNGPW3G5abkiZ28HD8kyUL5JdiLl7ZAM/ATwTzZW4mZ2vw==" type="application/javascript" data-module-id="./chunk-emoji-picker-element.js" data-src="https://github.githubassets.com/assets/chunk-emoji-picker-element-959f8a23.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-euLLeTFpj2DeM/lF0qLZedbrh2iLKL86jMNj8ydBs0Dr24s0ZxmdYnenUo2UIVD8r3t2DgXaahNQmstHlXpmtA==" type="application/javascript" data-module-id="./chunk-extent.js" data-src="https://github.githubassets.com/assets/chunk-extent-7ae2cb79.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-wsUwgwxED8pP99OX+oHo/gihRkaVCoUOuKeuca5uSpYTkOdSpJJSQr0ERYaQU9/pW2LO17/5kSLM4dBNFd8kWQ==" type="application/javascript" data-module-id="./chunk-failbot.js" data-src="https://github.githubassets.com/assets/chunk-failbot-c2c53083.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-vu9Jz7uYqWEzuZt9vTxZhokIyojtlOeJeuKlm9VXk9X+D0mEbs4wZrBFvaOuIGUfYLD+cWL87P3uWLWu4ddocA==" type="application/javascript" data-module-id="./chunk-feature-callout-element.js" data-src="https://github.githubassets.com/assets/chunk-feature-callout-element-beef49cf.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-5r/m4Q9I8PFeDYmfZIE5Nmi+ua6kmrqzCpKXwr/9uKdNZe3Vcywf3vzVHxc8ggzU8ujHJqGIMTZXF/E2N+tFtg==" type="application/javascript" data-module-id="./chunk-file-filter-element.js" data-src="https://github.githubassets.com/assets/chunk-file-filter-element-e6bfe6e1.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-8mFWnW8tKukTuJ5KV8c3133BhxXt/Mmp0KD3ge9pWKcejZxB8STIx9vOeyM/Nzysu8c5EFjHB1K5FTbRar90Rw==" type="application/javascript" data-module-id="./chunk-file-filter-persistence.js" data-src="https://github.githubassets.com/assets/chunk-file-filter-persistence-f261569d.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-oKiV7L6PsUGMFeoseGl5JsrDAEfonVuBLWBp7nZ7AbCVBtc5NSrE+pkZpbAaSTrW3ZfMf24oqAbzcc8XUdt3Yw==" type="application/javascript" data-module-id="./chunk-file-tree-element.js" data-src="https://github.githubassets.com/assets/chunk-file-tree-element-a0a895ec.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-HmlTAbYYypu6xIfkc5lZknDVCpWNWBWqotVdG16NPCcFVn1eCQMAjQZMgYtwONmU97MwJ3QBSjlj3RZpBI8QcQ==" type="application/javascript" data-module-id="./chunk-file-tree-toggle-element.js" data-src="https://github.githubassets.com/assets/chunk-file-tree-toggle-element-1e695301.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-1njRxGWK/1YwlIgBa4NNAJixjlS9EmfPdTPnDSw+H9qYm7JbF4wICBAJok9PJgX9iIvPcCFLr4+9VWa3aS6UGA==" type="application/javascript" data-module-id="./chunk-filter-input.js" data-src="https://github.githubassets.com/assets/chunk-filter-input-d678d1c4.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-PnU+sfTXdyJ04N6yBgLo5Z2SjobVkjg3KeIMPPFahdKGVHIjIB5qXL0Lyc251ZrlqGoiZy6pFaPeK5zn4MGjKg==" type="application/javascript" data-module-id="./chunk-format-symbol.js" data-src="https://github.githubassets.com/assets/chunk-format-symbol-3e753eb1.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-I3f3Mg+8lKnfufPcdki3NWiXyR/WOJ2EQCE+IlCS0OzAZ/9/YzYJ5v+9qUAZNyHB8eS7M0CCARJ1nQCjlHe8mQ==" type="application/javascript" data-module-id="./chunk-get-repo-element.js" data-src="https://github.githubassets.com/assets/chunk-get-repo-element-2377f732.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-1YyRxy7P1eKjAsJP+/J5r58i7pUkqQV1iLcEi8BM8mXtvgkCx5oGBTsTCXY7kNxZwdM89wuW0bUqEmT/K2pAmA==" type="application/javascript" data-module-id="./chunk-index.esm.js" data-src="https://github.githubassets.com/assets/chunk-index.esm-d58c91c7.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-l1nMNuiARJ5TD7tYJoxL9CWJpuRIQizQB5Yow6uYdQLjHF+jhlhjIRCOkjlwu2cPdw5IZjD4cR21hGYyX4fQ2w==" type="application/javascript" data-module-id="./chunk-index.js" data-src="https://github.githubassets.com/assets/chunk-index-9759cc36.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-qOUpd16ML/w+JHQ+AgsVZx091bwb/LDsyH4VCFRjcgYSyvOX3C9sKGbPD71wRrLGXuAVmZMhW/rHxciExPYJhg==" type="application/javascript" data-module-id="./chunk-index2.js" data-src="https://github.githubassets.com/assets/chunk-index2-a8e52977.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-QNDWaHxe34aiO2cy7YLEP+JwDSLTn2f6XbiLs57XjWDv+fCEsKSju2pBNnbQ0gW1BNvmnKTdFm3a0Bfks7G8cg==" type="application/javascript" data-module-id="./chunk-index3.js" data-src="https://github.githubassets.com/assets/chunk-index3-40d0d668.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-/lTFJkfTffOvpQ3Fs6eq02kNzMlBwxwonQU6if7W0VbA7+7Kq2zWUUlX8iVH0/oA8DcVVps3tP5lFqBr/6oj6g==" type="application/javascript" data-module-id="./chunk-index4.js" data-src="https://github.githubassets.com/assets/chunk-index4-fe54c526.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-Ntnd0/5ZBGVRYTRI3XtP6vjjlgg5MyYB+mTrkAR16+nHItQyS+EVU5IeydLg7OtU30Xk85euBkFABjLw4BmU1g==" type="application/javascript" data-module-id="./chunk-index5.js" data-src="https://github.githubassets.com/assets/chunk-index5-36d9ddd3.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-MS1Zii7vEXvNGfCzfot3Ay7Rb4jDjjTve/4lJs0ZVeznfQClBiTPhjvURBIH+eaoHprIg+ajqeamiG2/TNkKFQ==" type="application/javascript" data-module-id="./chunk-index6.js" data-src="https://github.githubassets.com/assets/chunk-index6-312d598a.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-PzguLzCZSX4+hasAu7u8YDVWgFv/0OVZooA+vfjBMr3TYfRwT+DCbLq3B08j4ntyYKddfGSKJjfh4r4bVz3YyQ==" type="application/javascript" data-module-id="./chunk-index7.js" data-src="https://github.githubassets.com/assets/chunk-index7-3f382e2f.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-97hqkbIvwW7HJzpWnhaTFrvWSA/scr+5o7FqPsphio+ngTnkbV6LlA0PE5jFHs15vOVqtJvkHHpYL0iIITjgjA==" type="application/javascript" data-module-id="./chunk-input-demux.js" data-src="https://github.githubassets.com/assets/chunk-input-demux-f7b86a91.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-4ZToQVMOXo8sxNzItJtpJQ/aBNgkzSVfq2YGbUQnbX59DpBemMGOuph6ShQgeRcuJk+x92FKYlhl92AbejD+ww==" type="application/javascript" data-module-id="./chunk-insights-query.js" data-src="https://github.githubassets.com/assets/chunk-insights-query-e194e841.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-Mma9eU389bpaBMusL0AOdyVXlum506TbS103AlnuSSzmGYEPNtSmgFlSPx5S5wxJmj1Wc1NGtCDvs71md1bapQ==" type="application/javascript" data-module-id="./chunk-invitations.js" data-src="https://github.githubassets.com/assets/chunk-invitations-3266bd79.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-l3pOrptLfUNxEwFeyOwmbxGTi/K9VocepNvqMGuuENiOtLDnNkhNV8Uc8Ufoqm0zp1KJOdhl1ggIF9JIXPlrkw==" type="application/javascript" data-module-id="./chunk-jump-to.js" data-src="https://github.githubassets.com/assets/chunk-jump-to-977a4eae.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-8Zr3D4tATIN9RgbnUQPSG6ynrNzIHEQBEC2X9FWxfXk4tbP4gp+ey/Qin4S/7Ey38XRxRg16Ut2fhSHkH1zA1g==" type="application/javascript" data-module-id="./chunk-launch-code-element.js" data-src="https://github.githubassets.com/assets/chunk-launch-code-element-f19af70f.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-92jpdKelNx62F7UBT82SokGtEavcA+2aKd7tNcefzagcDmCnjTk/8ffmZ24eOPBi62VW4CDooFMXLenxxWercA==" type="application/javascript" data-module-id="./chunk-line-chart.js" data-src="https://github.githubassets.com/assets/chunk-line-chart-f768e974.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-GHMEiXdvG00Lv7Tnj+S7/TnqlcyVi41j6xapftzfnYoGWz5iYCMK5XCoDFmCmSgliaA0pmVHO356D2u3zJCicw==" type="application/javascript" data-module-id="./chunk-line.js" data-src="https://github.githubassets.com/assets/chunk-line-18730489.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-SErVGzFh5d4RY684E3TP0k4oymFEXft5zG2STX8WWBVsYLU1CzKWKooMuhIGsL77HG7pyviD12Dy3zs0GN41bg==" type="application/javascript" data-module-id="./chunk-linear.js" data-src="https://github.githubassets.com/assets/chunk-linear-484ad51b.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-YUCb5GVAF8qPEnN/WtyP9j81k8qOlMzl35cLqVFLixJgBMqQ+ZT+ELoBUx2OTqs5IrYwqq9c+gk4O0qRN3h0EQ==" type="application/javascript" data-module-id="./chunk-locale.js" data-src="https://github.githubassets.com/assets/chunk-locale-61409be4.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-z5CnRrYFTqXt/cLpxeZbeOJFhX9E0mmje1Cf2cNNuGf8Wiu8zKxbOgH5o1gb2FL7PpCBcq4NWx+OR0J7h0eTjw==" type="application/javascript" data-module-id="./chunk-map.js" data-src="https://github.githubassets.com/assets/chunk-map-cf90a746.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-ptvLZkNg+C03ttOe2BfDaeurTiJY+zXDVgUaCzdTLlXVtlNo1JN5cijLL0vTxKncUtTavVi887fyRKhbW8eQPA==" type="application/javascript" data-module-id="./chunk-marketplace-insights-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-marketplace-insights-graph-element-a6dbcb66.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-tEvoyDbJMJRfri4FMBFNAfgpItBneOW/4YtlbCeLtjwnLvq6pP2U/HWuroWcfnkaXQggdprNIZIVNmdwz7Lu5g==" type="application/javascript" data-module-id="./chunk-memex-project-picker-element.js" data-src="https://github.githubassets.com/assets/chunk-memex-project-picker-element-b44be8c8.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-cvjyIYhR2ZkuFAXHYZSjPTc5wXYOdISgqbXw69CXpDXdxffXmXuzjCcGJNVk3mDNYsVH4Q9sb2UMNPFrNxxRUQ==" type="application/javascript" data-module-id="./chunk-metric-selection-element.js" data-src="https://github.githubassets.com/assets/chunk-metric-selection-element-72f8f221.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-wpN+s55e0JkuffVR++S87PjAhQog0M/U4+l4pD/Ps8w9yNma6Pdmeij+RTxCSdDzqjgC9knsjPpZ5+ohkRd4ww==" type="application/javascript" data-module-id="./chunk-min.js" data-src="https://github.githubassets.com/assets/chunk-min-c2937eb3.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-+C+U3GQMIfd4xTRuMutY0mInBQA6ttqvxHzA/8+K9YwSFjlMftzHIzdu6pfFYZw7L0gfsBqx3UtFchaNhU9xPA==" type="application/javascript" data-module-id="./chunk-monthly-spend-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-monthly-spend-graph-element-f82f94dc.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-aYNntJOZeBzyhsX35l/XAH5STic/eL+BLWcOEitDxJJdLPzhFCMC/uuVZkTr0uEk84PgB6OLeGNVhF1xh28v2w==" type="application/javascript" data-module-id="./chunk-navigation-list-element.js" data-src="https://github.githubassets.com/assets/chunk-navigation-list-element-698367b4.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-CVSejWt81gyND8tKvQOkpn87ow4VzsnRe+PjSwxHuMyyWxqdk69Jpj/cjhK3jeGUUcgn2CpMpRFpLpCf08KmfQ==" type="application/javascript" data-module-id="./chunk-network-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-network-graph-element-09549e8d.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-MYHfk4RC1G7um5oS3Cg8p/6FekxAiWQQvmCR526sy3/Yxbe6WEgDm5D64atvKXEqPps/0VgTxmSUH4XICbv5sw==" type="application/javascript" data-module-id="./chunk-nodrag.js" data-src="https://github.githubassets.com/assets/chunk-nodrag-3181df93.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-uBp/iTTm9wygkEp69MZdyvOA9r1CjfB/B6mvg5icD6kR3YsGNAF3+NXSJA08a6d71+XyhFU5471+c4aGHV42Sw==" type="application/javascript" data-module-id="./chunk-notification-list-focus.js" data-src="https://github.githubassets.com/assets/chunk-notification-list-focus-b81a7f89.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-/NlW6Pq0r1YJWymfejd89Z9JPNn1EIm7fu9AqR28Cy9dVmwJj9P4E1YMOPvnFLxIJ8Y5xdqBBdPX3qO8+h+2Mw==" type="application/javascript" data-module-id="./chunk-org-insights-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-org-insights-graph-element-fcd956e8.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-UpfXcE8D72JtkgF68l5LopywUMIDLi+ov+G9Kyaiz+zZUQxAXzu3jkIOJ5D0IaK7A54EOHWGpFSsMWnZQ+GsEQ==" type="application/javascript" data-module-id="./chunk-overview.js" data-src="https://github.githubassets.com/assets/chunk-overview-5297d770.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-tJgiApJcFJ0jL8UvfL7qx7j9aXTzPymdLhbbKlQtYOTijtqK9fMhJvW/dFkG4I27HcesAef/06xERFczvVOCvQ==" type="application/javascript" data-module-id="./chunk-package-dependencies-security-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-package-dependencies-security-graph-element-b4982202.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-rm1qIXRm4iMgRzHKiWNxs89dEXeQEvDZZ7qiYVFDhwbPBgNGl2Thwc/fSe8jjtq9eErkecWSDrFycssBZgoxyw==" type="application/javascript" data-module-id="./chunk-pointer.js" data-src="https://github.githubassets.com/assets/chunk-pointer-ae6d6a21.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-qEMigPltoBeFtlfHd0r2kjylnlwHjhf9+QfoggBvDF5uYSMtRBn1YvtRU7nwpoWRwtH/PQ/eFTNkSNKjQ1mauQ==" type="application/javascript" data-module-id="./chunk-premium-runners.js" data-src="https://github.githubassets.com/assets/chunk-premium-runners-a8432280.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-EbJJxBGp3rK2Vtkv8b2+hHIguudREKLm3SEWpr61TTjBnmruyJ3PzFc/mBHZby40YWLwm33opDhsCG4sVgTSjQ==" type="application/javascript" data-module-id="./chunk-presence-avatars.js" data-src="https://github.githubassets.com/assets/chunk-presence-avatars-11b249c4.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-5H5N/3G/20nmVKntphXb9z0H9q3URFDmHSccLhFkMSA8ILAA9mYlRKCWAWoDcl/W437jtGw1tIxjWStfInvidw==" type="application/javascript" data-module-id="./chunk-profile-pins-element.js" data-src="https://github.githubassets.com/assets/chunk-profile-pins-element-e47e4dff.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-vFR+IqThljOLrAWmjhOL/kiQrjgZZg95uPovX0J7kRH5p7Y049LDRZaXLMDijfeqqk71d3MMn9XP5bUcH+lB9w==" type="application/javascript" data-module-id="./chunk-profile.js" data-src="https://github.githubassets.com/assets/chunk-profile-bc547e22.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-rEl54d6O1BTVAm7SYyiHt/uzMMT2eTKFNw2w0wDIIunpTLtmq6QdgbIOF1t1Dm/8NQ8LFs7/TjM1qTR6hmUKyA==" type="application/javascript" data-module-id="./chunk-project-picker-element.js" data-src="https://github.githubassets.com/assets/chunk-project-picker-element-ac4979e1.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-MU7UjNfhOwMpfRSJ+AFgxtPNDENF6fScgs30W0liiQOAUXS4V+XcI2MQaun9+wQTxofnCiBFzTkhuLN2Jgtszw==" type="application/javascript" data-module-id="./chunk-pulse-authors-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-pulse-authors-graph-element-314ed48c.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-MU7VY0mux9rnjbuPVXGG86/+7UndHVzcSyt3JvD+cxDXvvPzpQA8k/XrZHykVBw+5qUSjjjAnQ5WD/T/q5EJng==" type="application/javascript" data-module-id="./chunk-range.js" data-src="https://github.githubassets.com/assets/chunk-range-314ed563.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-JDP9nIoagFBEBn3aXMHSL9s59qh0OWMhsg2xQJAwBYWS9q1PfZBor0UyNFJX6mFFXAHUvAIgnDiAKFw6OUJsiA==" type="application/javascript" data-module-id="./chunk-readme-toc-element.js" data-src="https://github.githubassets.com/assets/chunk-readme-toc-element-2433fd9c.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-4aLsPyiz8vqmHsO/bT8AF1ucYnON4JsLOfK5rD85xxOWbSpjet1Ljn4lIy+c/Un7AawwEPW7MBiG+5u+JDD2aA==" type="application/javascript" data-module-id="./chunk-ref-selector.js" data-src="https://github.githubassets.com/assets/chunk-ref-selector-e1a2ec3f.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-rylM3uiZ0RoRl560qJv60gb35nFfvE8DRrVVYM3IAJQnjbqiewiw9KwY/3R3bdKp/ER3Knadmvc0xZWgjk8g3w==" type="application/javascript" data-module-id="./chunk-reload-after-polling-element.js" data-src="https://github.githubassets.com/assets/chunk-reload-after-polling-element-af294cde.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-xKURm42qNMhOZDJVV3Tr6qlBE8mKZbd2mekIX8Sevwe93QT1btqQSifbgqeKc57TOu7SLjJmHVb+eZxJxvzfdQ==" type="application/javascript" data-module-id="./chunk-remote-clipboard-copy.js" data-src="https://github.githubassets.com/assets/chunk-remote-clipboard-copy-c4a5119b.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-8ME7nLIXe5Oqqah8+VbsNkORdavh5B6Pddl9RvJGniLt1e85L3nu2N5yWhMaucy+pyqg3jUR0pJ7RI8nlNYDtA==" type="application/javascript" data-module-id="./chunk-remote-content-element.js" data-src="https://github.githubassets.com/assets/chunk-remote-content-element-f0c13b9c.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-lwVBrgolfkJsmzF0Pq7DQWA84scBWfKrbYvsJkld4RhieE7u3hPGQ+jcWN5g4cS8Vl8E6k28tAO86b1bMBiafw==" type="application/javascript" data-module-id="./chunk-responsive-underlinenav.js" data-src="https://github.githubassets.com/assets/chunk-responsive-underlinenav-970541ae.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-OtjCc7UezN3MvWiHOS/5lYkrBdHOAhcFrGD6/zMgTAugw5BSOaRrrux3wJxv9OlHHgxI32nOkesATHdRyucitA==" type="application/javascript" data-module-id="./chunk-runner-groups.js" data-src="https://github.githubassets.com/assets/chunk-runner-groups-3ad8c273.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-YT1sZoBexRNsvw2mnXAtdf87/5j3cL8ji/WS6h9F0mMh0wyUEx3EElel6roRMoI2Zq+bn5d1i8TSCeZJ84a6Rw==" type="application/javascript" data-module-id="./chunk-series-table.js" data-src="https://github.githubassets.com/assets/chunk-series-table-613d6c66.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-0ho0SIKf1TsQpvFNdpkKw57DmpU8LampLRvO67Q0G+6744f/qI8uTtL96F5tOPT56dG40cwoKB8v6kYqyGipvw==" type="application/javascript" data-module-id="./chunk-severity-calculator-element.js" data-src="https://github.githubassets.com/assets/chunk-severity-calculator-element-d21a3448.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-aVCinzyk7et6Yl7Swp8R2b9oxUBj8Usx4G/eLk+kaDr7kdk57F3SxXYHIaK6jTMBMpWRsRrdz8oQQhlnbCz50g==" type="application/javascript" data-module-id="./chunk-signalr-socket.js" data-src="https://github.githubassets.com/assets/chunk-signalr-socket-6950a29f.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-dFDltVJPgBJ+YpDMhcd3aDGmO08RmhPriPDYIDU+jAdZbWqbs4oD9PbZ+ebPjRdyhZxbRvFKOKtxqDsLciK+SQ==" type="application/javascript" data-module-id="./chunk-slug.js" data-src="https://github.githubassets.com/assets/chunk-slug-7450e5b5.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-SGxKZJPMoMDPJ4mVhReJ1NPmXxuTuePhizAUPkKphsivzZhVQstruqwewm3oUpP1yONOG8MITAodv/5iKRsEtw==" type="application/javascript" data-module-id="./chunk-sortable-behavior.js" data-src="https://github.githubassets.com/assets/chunk-sortable-behavior-486c4a64.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-roc/0cfaua9wDuXAOgLBYymh7ketXEgdvrXH5cKsDrwrHA8RdLZyyKvncKkwMTtAXvFBYnhOfxrRYJuu5kCyCQ==" type="application/javascript" data-module-id="./chunk-spoofed-commit-warning.js" data-src="https://github.githubassets.com/assets/chunk-spoofed-commit-warning-ae873fd1.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-n9CzyJxFxwIDn7201fJbWS0Pb+zHZ55ZREoB+DPm2fEEcVi6NQy9u74s28zd23c4HZcOQb+hgBHfx/evvTz0gg==" type="application/javascript" data-module-id="./chunk-stacked-area-chart.js" data-src="https://github.githubassets.com/assets/chunk-stacked-area-chart-9fd0b3c8.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-Z5vxYqlrzgKkUgwWnpxHQ7mGgyY4QVo6rX+t+/+TEiFrVv4hH0bIN7cl/YvFJ5FVrLz/LFu7mhSnEWByM5sJXw==" type="application/javascript" data-module-id="./chunk-stacks-input-config-view.js" data-src="https://github.githubassets.com/assets/chunk-stacks-input-config-view-679bf162.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-gmw7obKL/JEHWPp6zWFh+ynbXUFOidj1DN2aPiTDwP8Gair0moVuDmA340LD84A29I3ZPak19CEiumG+oIiseg==" type="application/javascript" data-module-id="./chunk-tag-input.js" data-src="https://github.githubassets.com/assets/chunk-tag-input-826c3ba1.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-0IOfDfOHJW06z0GwRYJjp03TxPkyF3OxjI4KP+rgd565nAqN0uN7QChz1+/v2/ueP2WXmWKOA6BA7byyMw2Lfw==" type="application/javascript" data-module-id="./chunk-three.module.js" data-src="https://github.githubassets.com/assets/chunk-three.module-d0839f0d.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-wbtDXrsp1UlaVwYqy/OhzlQoCcW05Y6X4Yij81VM9EVikXjOi1IFOj94YTV7/4pn8V0fzIC2tXTbqV3H9c215Q==" type="application/javascript" data-module-id="./chunk-time.js" data-src="https://github.githubassets.com/assets/chunk-time-c1bb435e.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-wIbptf1DKOsqdNtk6eFJNttwm/Rpkl3djUJp4AFKbFOJ29W4u19sJtGhVOQEgeCycpaRZKGuluEeSlilsTvV0A==" type="application/javascript" data-module-id="./chunk-tip.js" data-src="https://github.githubassets.com/assets/chunk-tip-c086e9b5.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-4GJz2wyWwjq7P4hyx3qSkjvnTO7RG5cWvnePVXPB+Oji6MBVugAdl7kCTKbpX8+Ae2ONvGJwFzSc9A7m1pqzXw==" type="application/javascript" data-module-id="./chunk-toast.js" data-src="https://github.githubassets.com/assets/chunk-toast-e06273db.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-ltLCW8IMbyitm42Birq6zurdnrQISouzbBpmdRjtSfspJQHfIU6K47VYlBYNFI+/WWyeOqCKX3gXJAkaYZUp8g==" type="application/javascript" data-module-id="./chunk-traffic-clones-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-traffic-clones-graph-element-96d2c25b.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-pVgjdqKHFObxyJ0mlVHj6JtCh2L+fyRrMXxhVXt6t/vInTDhfRiOrf5qNh6Ymqq92JjKyXNJbmOsy/LGm3o3LA==" type="application/javascript" data-module-id="./chunk-traffic-visitors-graph-element.js" data-src="https://github.githubassets.com/assets/chunk-traffic-visitors-graph-element-a5582376.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-zSAZt0KaQlTdiPwxtiJWRHdMz6uoW46PkM/zU78IyWQre/829J0AFfNUuHwXBihMmjDnlUF8k1DE3Ecqo4RtFg==" type="application/javascript" data-module-id="./chunk-traffic.js" data-src="https://github.githubassets.com/assets/chunk-traffic-cd2019b7.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-R+tG3SLlxMfqFe/QsCsVkiImlyr9aDIRGs81jLQFG/8IC/WqUcHWrS4KJdn93V23uBIhL1CStpD5WOGltedi9g==" type="application/javascript" data-module-id="./chunk-turbo.es2017-esm.js" data-src="https://github.githubassets.com/assets/chunk-turbo.es2017-esm-47eb46dd.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-rI2FdWWXcE56q7o7zcRQcCNa7donqsw3tMrn5WWG6lCwDRUiNUkFOWooJnZvh6lITRL+vV6jIOlZYFn5M+4stg==" type="application/javascript" data-module-id="./chunk-tweetsodium.js" data-src="https://github.githubassets.com/assets/chunk-tweetsodium-ac8d8575.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-ODZJzCJpaOfusrIka5QVZQcPiO9LBGyrrMYjhhJWSLuCN5WbZ5xiEiiOPOKVu71dqygyRdB2TY7AKPA1J5hqdg==" type="application/javascript" data-module-id="./chunk-unveil.js" data-src="https://github.githubassets.com/assets/chunk-unveil-383649cc.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-utEHDjun0CxOSh27/JBWAf9Fjm8RSD3RMwYCHp6/W5vxps0Yq0D8UDix9dnM5R2/II/APYfYm7PI8knjocveMA==" type="application/javascript" data-module-id="./chunk-user-status-submit.js" data-src="https://github.githubassets.com/assets/chunk-user-status-submit-bad1070e.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-6yI/t7GcFRajrquWdg5NqQdrvgI4rWRWcuZhNmAHH/T2aw2iB0uAco9nNYoETW3zzJ+tmnC7qqfArrHaYmk1oQ==" type="application/javascript" data-module-id="./chunk-voting.js" data-src="https://github.githubassets.com/assets/chunk-voting-eb223fb7.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-q34Q0/s/exmYECvsCRWCxp+22UY2cZK8MPrKv3LjI3bNU5AD3Fzv+JhN0Lgfvd2mgju3llixlQ4z2RvkTIw2oA==" type="application/javascript" data-module-id="./chunk-webgl-warp.js" data-src="https://github.githubassets.com/assets/chunk-webgl-warp-ab7e10d3.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-fhp8EDqbNbae6xwqU8vIxb89PjZnn5tMKAJRXukI4l3n/MMRnhDkQ0XLt1a8gcaHTOvJ0HTElC0eU8RPpMboYA==" type="application/javascript" src="https://github.githubassets.com/assets/optimizely-7e1a7c10.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-09crFTlFc+xYgbDcpuWpWFD5im/v+cvbUDuMdKvMw18TohuYXxKLzGcLEBgGPrZdwceheNEthOVzrFVD48rZkg==" type="application/javascript" src="https://github.githubassets.com/assets/codespaces-d3d72b15.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-MMkWfJssHf0Q/qwcMAnmcBMNXS5C9IxH0PkKrnGOYdDhewzD6Rjc5SMkb5fOPr6IWrOENxMAl1yph+PnRwHOKA==" type="application/javascript" src="https://github.githubassets.com/assets/repositories-30c9167c.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-5VS9txZOv3EOORFwDsEW5xPehMoVpb3tjrCYKqB6a0uAXGb8ZEa7AO2m0SLYFWh29wlXJyIHrMdi9YKaKpN2vw==" type="application/javascript" src="https://github.githubassets.com/assets/topic-suggestions-e554bdb7.js"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-Y9QCffkHDk3/KAoYUMhKeokbNlXWgpO+53XrccRwhUWzMTxEmhnp1ce7OVWP3vOzhCfWaxxnKWW9eVjjny8nRA==" type="application/javascript" src="https://github.githubassets.com/assets/code-menu-63d4027d.js"></script>
  

  <meta name="viewport" content="width=device-width">
  
  <title>rmenegaux/fastDNA</title>
    <meta name="description" content="Contribute to rmenegaux/fastDNA development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">
  <meta name="apple-itunes-app" content="app-id=1477376905" />
    <meta name="twitter:image:src" content="https://opengraph.githubassets.com/b6aa674ab0d98d0ebbcf43941c94b480004dd2aa173e1a5ce7de9dc0a378a5a5/rmenegaux/fastDNA" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="rmenegaux/fastDNA" /><meta name="twitter:description" content="Contribute to rmenegaux/fastDNA development by creating an account on GitHub." />
    <meta property="og:image" content="https://opengraph.githubassets.com/b6aa674ab0d98d0ebbcf43941c94b480004dd2aa173e1a5ce7de9dc0a378a5a5/rmenegaux/fastDNA" /><meta property="og:image:alt" content="Contribute to rmenegaux/fastDNA development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="rmenegaux/fastDNA" /><meta property="og:url" content="https://github.com/rmenegaux/fastDNA" /><meta property="og:description" content="Contribute to rmenegaux/fastDNA development by creating an account on GitHub." />
    



    

  <link rel="assets" href="https://github.githubassets.com/">
    <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/14911686/ws?session=eyJ2IjoiVjMiLCJ1IjoxNDkxMTY4NiwicyI6ODM5NzM4Mjg3LCJjIjozOTc3MDA2OTQyLCJ0IjoxNjQ2MjA3NDU0fQ==--4025a2681f43af414dc1aa3f4cd6cdb47fce2e4d426e19c5d8603dbbb562b644" data-refresh-url="/_alive" data-session-id="5b632c553eb895b8d1ca03912db208099eed1326cde9ef99cdbea88da009b6b9">
    <link rel="shared-web-socket-src" href="/assets-cdn/worker/socket-worker-941b4c1e.js">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

  <meta name="request-id" content="E627:DCFA:42A2B7:4B17C8:621F21DD" data-pjax-transient="true" /><meta name="html-safe-nonce" content="51f92d53b7863bbdbc52cca80398ce043c81d8f17e5415bf81f5fc7eee873bd6" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6bnVsbCwicmVxdWVzdF9pZCI6IkU2Mjc6RENGQTo0MkEyQjc6NEIxN0M4OjYyMUYyMUREIiwidmlzaXRvcl9pZCI6IjcyMjYyOTk5OTYzMjI2MDM0NTciLCJyZWdpb25fZWRnZSI6ImZyYSIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-pjax-transient="true" /><meta name="visitor-hmac" content="60183259b9c811714d1ed22662ef67f69826d48590cecd88d5dfe3f772efde8a" data-pjax-transient="true" />

    <meta name="hovercard-subject-tag" content="repository:152992660" data-pjax-transient>


  <meta name="github-keyboard-shortcuts" content="repository" data-pjax-transient="true" />

  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" /><meta name="octolytics-actor-id" content="14911686" /><meta name="octolytics-actor-login" content="phenolophthaleinum" /><meta name="octolytics-actor-hash" content="486d21ae2eb846e2b9a76f7a546aa15f37c31d617c3d0472641e740ff114bb61" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-pjax-transient="true" />

  




  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="phenolophthaleinum">


      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="Yjg1Y2ExYjNhMDQwZWNmODU1OGUxOTEyZTYyZDY0YTE2NTU0M2ZiY2U2YTM5ZDYxN2NmNGVkYTkyNmEyNzQ5NXx7InJlbW90ZV9hZGRyZXNzIjoiMTg4LjQ3LjExOC4xNTQiLCJyZXF1ZXN0X2lkIjoiRTYyNzpEQ0ZBOjQyQTJCNzo0QjE3Qzg6NjIxRjIxREQiLCJ0aW1lc3RhbXAiOjE2NDYyMDc0NTQsImhvc3QiOiJnaXRodWIuY29tIn0=">
      <meta name="keyboard-shortcuts-preference" content="all">
      <script type="application/json" id="memex_keyboard_shortcuts_preference">"all"</script>

    <meta name="enabled-features" content="ACTIONS_CALLABLE_WORKFLOWS,MARKETPLACE_PENDING_INSTALLATIONS,PRESENCE_IDLE">


  <meta http-equiv="x-pjax-version" content="eb7c63f3e9bfdef8e74888bd44617853c466aa4636927a9c1e8f8694cd59c951" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="ad743a89372c421844ffcba4fd906096b07b7fd7c2a57617ff2d2f0fdf463e56" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="51838b7fac5685cca82289cc316f3e63602d0444a5a3e71d164d478e1fbd31d3" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="ae44e83aa0600fc5c0edab81ad191180aeb9c0a55c6523c277c5ff962bb46249" data-turbo-track="reload">
  

    
  <meta name="go-import" content="github.com/rmenegaux/fastDNA git https://github.com/rmenegaux/fastDNA.git">

  <meta name="octolytics-dimension-user_id" content="9288961" /><meta name="octolytics-dimension-user_login" content="rmenegaux" /><meta name="octolytics-dimension-repository_id" content="152992660" /><meta name="octolytics-dimension-repository_nwo" content="rmenegaux/fastDNA" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="152992660" /><meta name="octolytics-dimension-repository_network_root_nwo" content="rmenegaux/fastDNA" />



    <link rel="canonical" href="https://github.com/rmenegaux/fastDNA" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="dark light" />

  <meta name="msapplication-TileImage" content="/windows-tile.png">
  <meta name="msapplication-TileColor" content="#ffffff">

  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive" style="word-wrap: break-word;">
    

    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader js-pjax-loader-bar Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      


        <script crossorigin="anonymous" defer="defer" integrity="sha512-12lPEVmJ9nfKESXT/8LlsWHh7hr+MJ0goPw5EfR/oBogDMGq+/pSfl1XmN9TcUQw+nHgm8HKw14S4xPYDf905w==" type="application/javascript" src="https://github.githubassets.com/assets/command-palette-d7694f11.js"></script>

            <header class="Header js-details-container Details px-3 px-md-4 px-lg-5 flex-wrap flex-md-nowrap" role="banner" >
    <div class="Header-item mt-n1 mb-n1  d-none d-md-flex">
      <a
  class="Header-link "
  href="https://github.com/"
  data-hotkey="g d"
  aria-label="Homepage "
  data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="9cf24bbea1267f7d30bd774da8b7ed3b2fa60c2420a37a1bc72ab4e3dac0efc9" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}"
>
  <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>

    </div>

    <div class="Header-item d-md-none">
      <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="Header-link js-details-target btn-link">  <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-three-bars">
    <path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path>
</svg>
</button>    </div>

    <div class="Header-item Header-item--full flex-column flex-md-row width-full flex-order-2 flex-md-order-none mr-0 mr-md-3 mt-3 mt-md-0 Details-content--hidden-not-important d-md-flex">
          



<div class="header-search flex-auto js-site-search position-relative flex-self-stretch flex-md-self-auto mb-3 mb-md-0 mr-0 mr-md-3 scoped-search site-scoped-search js-jump-to"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="152992660" data-scoped-search-url="/rmenegaux/fastDNA/search" data-owner-scoped-search-url="/users/rmenegaux/search" data-unscoped-search-url="/search" action="/rmenegaux/fastDNA/search" accept-charset="UTF-8" method="get">
      <label class="form-control input-sm header-search-wrapper p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey=s,/
          name="q"
          data-test-selector="nav-search-input"
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          role="combobox"
          aria-haspopup="listbox"
          aria-expanded="false"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
        >
        <input type="hidden" value="K1nobws2i-N8XqjxyzcMZBZ3tzc27xP_ELLt4y7a3v1mfTwl6OjP-3i95WGDtA-e-YDSFUcMajqxONjYtsNSdg" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />
        <input type="hidden" class="js-site-search-type-field" name="type" >
            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="20" aria-hidden="true" class="mr-1 header-search-key-slash"><path fill="none" stroke="#979A9C" opacity=".4" d="M3.5.5h12c1.7 0 3 1.3 3 3v13c0 1.7-1.3 3-3 3h-12c-1.7 0-3-1.3-3-3v-13c0-1.7 1.3-3 3-3z"></path><path fill="#979A9C" d="M11.8 6L8 15.1h-.9L10.8 6h1z"></path></svg>


          <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
            
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="suggestion">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="color-fg-muted">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-owner-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="owner_scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this user">
        In this user
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" data-item-type="global_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg title="Repository" aria-label="Repository" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo js-jump-to-octicon-repo d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
      <svg title="Project" aria-label="Project" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-project js-jump-to-octicon-project d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path>
</svg>
      <svg title="Search" aria-label="Search" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search js-jump-to-octicon-search d-none flex-shrink-0">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-2 flex-shrink-0 color-bg-subtle px-1 color-fg-muted ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="m-3 anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
    </li>
</ul>

          </div>
      </label>
</form>  </div>
</div>

        <nav class="d-flex flex-column flex-md-row flex-self-stretch flex-md-self-auto" aria-label="Global">
      <a class="Header-link py-md-3 d-block d-md-none py-2 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
        Dashboard
</a>
    <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
        Pull<span class="d-inline d-md-none d-lg-inline"> request</span>s
</a>
    <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
      Issues
</a>
      <div class="d-flex position-relative">
        <a class="js-selected-navigation-item Header-link flex-auto mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
          Marketplace
</a>      </div>

    <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
      Explore
</a>
    <a class="js-selected-navigation-item Header-link d-block d-md-none py-2 py-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:workspaces context:user" data-selected-links="/codespaces /codespaces" href="/codespaces">
      Codespaces
</a>
      <a class="js-selected-navigation-item Header-link d-block d-md-none py-2 py-md-3 border-top border-md-top-0 border-white-fade" data-ga-click="Header, click, Nav menu - item:Sponsors" data-hydro-click="{&quot;event_type&quot;:&quot;sponsors.button_click&quot;,&quot;payload&quot;:{&quot;button&quot;:&quot;HEADER_SPONSORS_DASHBOARD&quot;,&quot;sponsorable_login&quot;:&quot;phenolophthaleinum&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8aeea7a633a962338da825342600b983620cdf36a493f0ef675bd9a8a9167aeb" data-selected-links=" /sponsors/accounts" href="/sponsors/accounts">Sponsors</a>

    <a class="Header-link d-block d-md-none mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade" href="/settings/profile">
      Settings
</a>
    <a class="Header-link d-block d-md-none mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade" href="/phenolophthaleinum">
      <img class="avatar avatar-user" loading="lazy" decoding="async" src="https://avatars.githubusercontent.com/u/14911686?s=40&amp;v=4" width="20" height="20" alt="@phenolophthaleinum" />
      phenolophthaleinum
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="4g2jU9d7vGCMIXFuUsW21VaDHoTCMxJggMMGxUJ1AhC9yvc5yDZsUV6hxqLLoL6t6kewYCO8EERtwi9P73dGtA" />
      <button
        type="submit"
        class="Header-link mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade d-md-none btn-link d-block width-full text-left"
        style="padding-left: 2px;"
        data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;sign out&quot;,&quot;label&quot;:&quot;icon:logout&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="ed0e60e09eeb567e27cea5f9a81fcc0237c5068b0a070dc8a7723fe2a8bc4f3d" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;sign out&quot;,&quot;label&quot;:&quot;icon:logout&quot;}"
      >
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sign-out v-align-middle">
    <path fill-rule="evenodd" d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 010 1.5h-2.5a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 010 1.5h-2.5A1.75 1.75 0 012 13.25V2.75zm10.44 4.5H6.75a.75.75 0 000 1.5h5.69l-1.97 1.97a.75.75 0 101.06 1.06l3.25-3.25a.75.75 0 000-1.06l-3.25-3.25a.75.75 0 10-1.06 1.06l1.97 1.97z"></path>
</svg>
        Sign out
      </button>
</form></nav>

    </div>

    <div class="Header-item Header-item--full flex-justify-center d-md-none position-relative">
        <a
  class="Header-link "
  href="https://github.com/"
  data-hotkey="g d"
  aria-label="Homepage "
  data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="9cf24bbea1267f7d30bd774da8b7ed3b2fa60c2420a37a1bc72ab4e3dac0efc9" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}"
>
  <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>

    </div>

    <div class="Header-item mr-0 mr-md-3 flex-order-1 flex-md-order-none">
        


      <notification-indicator
        class="js-socket-channel"
        data-test-selector="notifications-indicator"
        data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTQ5MTE2ODYiLCJ0IjoxNjQ2MjA3NDU0fQ==--1062b70e1ec7599d9b61468dceeaf55297f1f4e22c2e9f949ac6bbd2ad421db0">
        <a href="/notifications"
          class="Header-link notification-indicator position-relative tooltipped tooltipped-sw"
          
          aria-label="You have no unread notifications"
          data-hotkey="g n"
          data-ga-click="Header, go to notifications, icon:read"
          data-target="notification-indicator.link">
          <span class="mail-status  " data-target="notification-indicator.modifier"></span>
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell">
    <path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path>
</svg>
        </a>
      </notification-indicator>

    </div>


    <div class="Header-item position-relative d-none d-md-flex">
        <details class="details-overlay details-reset">
  <summary
    class="Header-link"
    aria-label="Create new…"
    data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;create new&quot;,&quot;label&quot;:&quot;icon:add&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="e80f1cbb1bcee7052a2d4858db88912b982d3f52188e941eecf0faea8c3f5f1a" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;create new&quot;,&quot;label&quot;:&quot;icon:add&quot;}"
  >
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path fill-rule="evenodd" d="M7.75 2a.75.75 0 01.75.75V7h4.25a.75.75 0 110 1.5H8.5v4.25a.75.75 0 11-1.5 0V8.5H2.75a.75.75 0 010-1.5H7V2.75A.75.75 0 017.75 2z"></path>
</svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  </details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0 d-none d-md-flex">
        
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/phenolophthaleinum/feature_preview/indicator_check">

  <summary
    class="Header-link"
    aria-label="View profile and more"
    data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;show menu&quot;,&quot;label&quot;:&quot;icon:avatar&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="1d1ffd91054c0308926b2b014de7d7872fe51c87a89d5dfd92ae0c81b198e5c1" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;show menu&quot;,&quot;label&quot;:&quot;icon:avatar&quot;}"
  >
    <img src="https://avatars.githubusercontent.com/u/14911686?s=40&amp;v=4" alt="@phenolophthaleinum" size="20" height="20" width="20" data-view-component="true" class="avatar avatar-small circle" />
      <span class="feature-preview-indicator js-feature-preview-indicator" style="top: 1px;" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu
      class="dropdown-menu dropdown-menu-sw"
      style="width: 180px"
      
      preload>
      <include-fragment src="/users/14911686/menu" loading="lazy">
        <p class="text-center mt-3" data-hide-on-error>
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
        </p>
        <p class="ml-1 mb-2 mt-2 color-fg-default" data-show-on-error>
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
          Sorry, something went wrong.
        </p>
      </include-fragment>
  </details-menu>
</details>

    </div>
</header>

            
    </div>

  <div id="start-of-content" class="show-on-focus"></div>







    <div data-pjax-replace id="js-flash-container">


  <template class="js-flash-template">
    <div class="flash flash-full  {{ className }}">
  <div class="px-2" >
    <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
    </button>
    
      <div>{{ message }}</div>

  </div>
</div>
  </template>
</div>


    

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




      <details class="details-reset details-overlay details-overlay-dark js-command-palette-dialog">
  <summary class="command-palette-details-summary" aria-label="command palette trigger">
  </summary>
  <details-dialog class="command-palette-details-dialog d-flex flex-column flex-justify-center height-fit" aria-label="command palette">
    <command-palette
      class="command-palette color-bg-default rounded-3"
      data-return-to=/rmenegaux/fastDNA
      data-user-id="14911686"
      data-activation-hotkey="Mod+k,Mod+Alt+k"
      data-command-mode-hotkey="Mod+Shift+k"
      >

      <input type="hidden" name="color-mode-path" id="color-mode-path" value="/settings/appearance/color_mode" class="js-color-mode-path" autocomplete="off" />
      <input type="hidden" value="sBaZRnUS0hUKYQc16bovrpC4q9fJCPtexYcQFQgNEMH8JxTNSsBKIlxpn8pn-pwj3_m9eItThXaWKYaInGRumQ" data-csrf="true" class="js-color-mode-csrf" />

        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search issues and pull requests"
        ></command-palette-mode>
        <command-palette-mode
          data-char="#"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search issues, pull requests, discussions, and projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="!"
            data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
            data-placeholder="Search projects"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;&quot;]"
            data-placeholder="Search or jump to a user, organization, or repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="@"
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to a repository"
        ></command-palette-mode>
        <command-palette-mode
          data-char="/"
            data-scope-types="[&quot;repository&quot;]"
            data-placeholder="Search files"
        ></command-palette-mode>
        <command-palette-mode
          data-char="?"
        ></command-palette-mode>
        <command-palette-mode
          data-char="&gt;"
            data-placeholder="Run a command"
        ></command-palette-mode>
        <command-palette-mode
          data-char=""
            data-scope-types="[&quot;owner&quot;]"
            data-placeholder="Search or jump to..."
        ></command-palette-mode>
      <command-palette-mode
        class="js-command-palette-default-mode"
        data-char=""
        data-placeholder="Search or jump to..."
      ></command-palette-mode>

      <command-palette-input placeholder="Search or jump to..."
      >
        <div class="js-search-icon d-flex flex-items-center mr-2" style="height: 26px">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search color-fg-muted">
    <path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path>
</svg>
        </div>
        <div class="js-spinner d-flex flex-items-center mr-2 color-fg-muted" hidden>
          <svg aria-label="Loading" class="anim-rotate" viewBox="0 0 16 16" fill="none" width="16" height="16">
            <circle
              cx="8"
              cy="8"
              r="7"
              stroke="currentColor"
              stroke-opacity="0.25"
              stroke-width="2"
              vector-effect="non-scaling-stroke"
            ></circle>
            <path
              d="M15 8a7.002 7.002 0 00-7-7"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              vector-effect="non-scaling-stroke"
            ></path>
          </svg>
        </div>
        <command-palette-scope >
          <div data-target="command-palette-scope.placeholder" hidden class="color-fg-subtle">/&nbsp;&nbsp;<span class="text-semibold color-fg-default">...</span>&nbsp;&nbsp;/&nbsp;&nbsp;</div>
              <command-palette-token
                data-text="rmenegaux"
                data-id="MDQ6VXNlcjkyODg5NjE="
                data-type="owner"
                data-value="rmenegaux"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >rmenegaux<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
              <command-palette-token
                data-text="fastDNA"
                data-id="MDEwOlJlcG9zaXRvcnkxNTI5OTI2NjA="
                data-type="repository"
                data-value="fastDNA"
                data-targets="command-palette-scope.tokens"
                class="color-fg-default text-semibold"
                style="white-space:nowrap;line-height:20px;"
                >fastDNA<span class="color-fg-subtle text-normal">&nbsp;&nbsp;/&nbsp;&nbsp;</span></command-palette-token>
        </command-palette-scope>
        <div class="command-palette-input-group flex-1 form-control border-0 box-shadow-none" style="z-index: 0">
          <div class="command-palette-typeahead position-absolute d-flex flex-items-center Truncate">
            <span class="typeahead-segment input-mirror" data-target="command-palette-input.mirror"></span>
            <span class="Truncate-text" data-target="command-palette-input.typeaheadText"></span>
            <span class="typeahead-segment" data-target="command-palette-input.typeaheadPlaceholder"></span>
          </div>
          <input
            class="js-overlay-input typeahead-input d-none"
            disabled
            tabindex="-1"
            aria-label="Hidden input for typeahead"
          >
          <input
            type="text"
            autocomplete="off"
            autocorrect="off"
            autocapitalize="off"
            spellcheck="false"
            class="js-input typeahead-input form-control border-0 box-shadow-none input-block width-full"
            aria-label="Command palette input"
            aria-haspopup="listbox"
            aria-expanded="false"
            aria-autocomplete="list"
            aria-controls="command-palette-item-stack"
            role="combobox"
          >
        </div>
        <button aria-label="clear command palette" aria-keyshortcuts="Control+Backspace" id="command-palette-clear-button" type="button" data-view-component="true" class="btn-octicon js-clear command-palette-input-clear-button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill">
    <path fill-rule="evenodd" d="M2.343 13.657A8 8 0 1113.657 2.343 8 8 0 012.343 13.657zM6.03 4.97a.75.75 0 00-1.06 1.06L6.94 8 4.97 9.97a.75.75 0 101.06 1.06L8 9.06l1.97 1.97a.75.75 0 101.06-1.06L9.06 8l1.97-1.97a.75.75 0 10-1.06-1.06L8 6.94 6.03 4.97z"></path>
</svg></button>
        <primer-tooltip hidden="hidden" for="command-palette-clear-button" data-direction="w" data-type="description" data-view-component="true">Clear</primer-tooltip>
      </command-palette-input>

        <command-palette-item-stack id="command-palette-item-stack" class="item-stack-transition-height"  role="listbox" aria-label="Command palette results">
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type <kbd class="hx_kbd">#</kbd> to search pull requests
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type <kbd class="hx_kbd">#</kbd> to search issues
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
                data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type <kbd class="hx_kbd">#</kbd> to search discussions
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
                data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type <kbd class="hx_kbd">!</kbd> to search projects
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
                data-scope-types="[&quot;owner&quot;]"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type <kbd class="hx_kbd">@</kbd> to search teams
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
                data-scope-types="[&quot;&quot;]"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type <kbd class="hx_kbd">@</kbd> to search people and organizations
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type <kbd class="hx_kbd">&gt;</kbd> to activate command mode
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode=""
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Go to your accessibility settings to change your keyboard shortcuts
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode="#"
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type author:@me to search your content
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode="#"
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type is:pr to filter to pull requests
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode="#"
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type is:issue to filter to issues
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
                data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
              data-mode="#"
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type is:project to filter to projects
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
            <command-palette-tip
              class="color-fg-muted f6 px-3 py-1 my-2"
              data-mode="#"
              data-value="">
              <div class="d-flex flex-items-start flex-justify-between">
                <div>
                  <span class="text-bold">Tip:</span>
                    Type is:open to filter to open content
                </div>
                <div class="ml-2 flex-shrink-0">
                  Type <kbd class="hx_kbd">?</kbd> for help and tips
                </div>
              </div>
            </command-palette-tip>
          <command-palette-tip class="mx-3 my-2 flash flash-error d-flex flex-items-center" data-on-error>
            <div>
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
            </div>
            <div class="px-2">
              We’ve encountered an error and some results aren't available at this time. Type a new search or try again later.
            </div>
          </command-palette-tip>
          <command-palette-tip class="h4 color-fg-default pl-3 pb-2 pt-3" data-on-empty data-match-mode="[^?]|^$">
            No results matched your search
          </command-palette-tip>

            <command-palette-item-group
              data-group-id="top"
              data-group-title="Top result"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="commands"
              data-group-title="Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="global_commands"
              data-group-title="Global Commands"
              data-group-hint="Type &gt; to filter"
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="files"
              data-group-title="Files"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="pages"
              data-group-title="Pages"
              data-group-hint=""
              data-group-limits="{&quot;repository&quot;:10}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="access_policies"
              data-group-title="Access Policies"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="organizations"
              data-group-title="Organizations"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="repositories"
              data-group-title="Repositories"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="references"
              data-group-title="Issues, pull requests, and discussions"
              data-group-hint="Type # to filter"
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="teams"
              data-group-title="Teams"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="users"
              data-group-title="Users"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="projects"
              data-group-title="Projects"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="footer"
              data-group-title="Footer"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="modes_help"
              data-group-title="Modes"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
            <command-palette-item-group
              data-group-id="filters_help"
              data-group-title="Use filters in issues, pull requests, discussions, and projects"
              data-group-hint=""
              data-group-limits="{}"
              data-targets="command-palette-item-stack.groups"
            >
            </command-palette-item-group>
        </command-palette-item-stack>

      <div class="js-command-local-provider-octicons" hidden>
          <div data-local-provider-octicon-id="arrow-right-color-fg-muted">
            <svg height="16" class="octicon octicon-arrow-right color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="arrow-right-color-fg-default">
            <svg height="16" class="octicon octicon-arrow-right color-fg-default" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="codespaces-color-fg-muted">
            <svg height="16" class="octicon octicon-codespaces color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 1.75C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 01-1.75 1.75h-8.5A1.75 1.75 0 012 6.75v-5zm1.75-.25a.25.25 0 00-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25v-5a.25.25 0 00-.25-.25h-8.5zM0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0114.25 16H1.75A1.75 1.75 0 010 14.25v-3zM1.75 11a.25.25 0 00-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25v-3a.25.25 0 00-.25-.25H1.75z"></path><path fill-rule="evenodd" d="M3 12.75a.75.75 0 01.75-.75h.5a.75.75 0 010 1.5h-.5a.75.75 0 01-.75-.75zm4 0a.75.75 0 01.75-.75h4.5a.75.75 0 010 1.5h-4.5a.75.75 0 01-.75-.75z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="copy-color-fg-muted">
            <svg height="16" class="octicon octicon-copy color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="dash-color-fg-muted">
            <svg height="16" class="octicon octicon-dash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 7.75A.75.75 0 012.75 7h10a.75.75 0 010 1.5h-10A.75.75 0 012 7.75z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="file-color-fg-muted">
            <svg height="16" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="lock-color-fg-muted">
            <svg height="16" class="octicon octicon-lock color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 4v2h-.25A1.75 1.75 0 002 7.75v5.5c0 .966.784 1.75 1.75 1.75h8.5A1.75 1.75 0 0014 13.25v-5.5A1.75 1.75 0 0012.25 6H12V4a4 4 0 10-8 0zm6.5 2V4a2.5 2.5 0 00-5 0v2h5zM12 7.5h.25a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-8.5a.25.25 0 01-.25-.25v-5.5a.25.25 0 01.25-.25H12z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="moon-color-fg-muted">
            <svg height="16" class="octicon octicon-moon color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.598 1.591a.75.75 0 01.785-.175 7 7 0 11-8.967 8.967.75.75 0 01.961-.96 5.5 5.5 0 007.046-7.046.75.75 0 01.175-.786zm1.616 1.945a7 7 0 01-7.678 7.678 5.5 5.5 0 107.678-7.678z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="person-color-fg-muted">
            <svg height="16" class="octicon octicon-person color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M10.5 5a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zm.061 3.073a4 4 0 10-5.123 0 6.004 6.004 0 00-3.431 5.142.75.75 0 001.498.07 4.5 4.5 0 018.99 0 .75.75 0 101.498-.07 6.005 6.005 0 00-3.432-5.142z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="pencil-color-fg-muted">
            <svg height="16" class="octicon octicon-pencil color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="issue-opened-open">
            <svg height="16" class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path><path fill-rule="evenodd" d="M8 0a8 8 0 100 16A8 8 0 008 0zM1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="git-pull-request-draft-color-fg-muted">
            <svg height="16" class="octicon octicon-git-pull-request-draft color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M2.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.25 1a2.25 2.25 0 00-.75 4.372v5.256a2.251 2.251 0 101.5 0V5.372A2.25 2.25 0 003.25 1zm0 11a.75.75 0 100 1.5.75.75 0 000-1.5zm9.5 3a2.25 2.25 0 100-4.5 2.25 2.25 0 000 4.5zm0-3a.75.75 0 100 1.5.75.75 0 000-1.5z"></path><path d="M14 7.5a1.25 1.25 0 11-2.5 0 1.25 1.25 0 012.5 0zm0-4.25a1.25 1.25 0 11-2.5 0 1.25 1.25 0 012.5 0z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="search-color-fg-muted">
            <svg height="16" class="octicon octicon-search color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="sun-color-fg-muted">
            <svg height="16" class="octicon octicon-sun color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 10.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5zM8 12a4 4 0 100-8 4 4 0 000 8zM8 0a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0V.75A.75.75 0 018 0zm0 13a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0v-1.5A.75.75 0 018 13zM2.343 2.343a.75.75 0 011.061 0l1.06 1.061a.75.75 0 01-1.06 1.06l-1.06-1.06a.75.75 0 010-1.06zm9.193 9.193a.75.75 0 011.06 0l1.061 1.06a.75.75 0 01-1.06 1.061l-1.061-1.06a.75.75 0 010-1.061zM16 8a.75.75 0 01-.75.75h-1.5a.75.75 0 010-1.5h1.5A.75.75 0 0116 8zM3 8a.75.75 0 01-.75.75H.75a.75.75 0 010-1.5h1.5A.75.75 0 013 8zm10.657-5.657a.75.75 0 010 1.061l-1.061 1.06a.75.75 0 11-1.06-1.06l1.06-1.06a.75.75 0 011.06 0zm-9.193 9.193a.75.75 0 010 1.06l-1.06 1.061a.75.75 0 11-1.061-1.06l1.06-1.061a.75.75 0 011.061 0z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="sync-color-fg-muted">
            <svg height="16" class="octicon octicon-sync color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.5a5.487 5.487 0 00-4.131 1.869l1.204 1.204A.25.25 0 014.896 6H1.25A.25.25 0 011 5.75V2.104a.25.25 0 01.427-.177l1.38 1.38A7.001 7.001 0 0114.95 7.16a.75.75 0 11-1.49.178A5.501 5.501 0 008 2.5zM1.705 8.005a.75.75 0 01.834.656 5.501 5.501 0 009.592 2.97l-1.204-1.204a.25.25 0 01.177-.427h3.646a.25.25 0 01.25.25v3.646a.25.25 0 01-.427.177l-1.38-1.38A7.001 7.001 0 011.05 8.84a.75.75 0 01.656-.834z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="trash-color-fg-muted">
            <svg height="16" class="octicon octicon-trash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="key-color-fg-muted">
            <svg height="16" class="octicon octicon-key color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 5.5a4 4 0 112.731 3.795.75.75 0 00-.768.18L7.44 10.5H6.25a.75.75 0 00-.75.75v1.19l-.06.06H4.25a.75.75 0 00-.75.75v1.19l-.06.06H1.75a.25.25 0 01-.25-.25v-1.69l5.024-5.023a.75.75 0 00.181-.768A3.995 3.995 0 016.5 5.5zm4-5.5a5.5 5.5 0 00-5.348 6.788L.22 11.72a.75.75 0 00-.22.53v2C0 15.216.784 16 1.75 16h2a.75.75 0 00.53-.22l.5-.5a.75.75 0 00.22-.53V14h.75a.75.75 0 00.53-.22l.5-.5a.75.75 0 00.22-.53V12h.75a.75.75 0 00.53-.22l.932-.932A5.5 5.5 0 1010.5 0zm.5 6a1 1 0 100-2 1 1 0 000 2z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="comment-discussion-color-fg-muted">
            <svg height="16" class="octicon octicon-comment-discussion color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="bell-color-fg-muted">
            <svg height="16" class="octicon octicon-bell color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path></svg>
          </div>
          <div data-local-provider-octicon-id="bell-slash-color-fg-muted">
            <svg height="16" class="octicon octicon-bell-slash color-fg-muted" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path></svg>
          </div>
      </div>

      <server-defined-provider data-type="search-links"></server-defined-provider>
      <server-defined-provider data-type="help">
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues</strong> and <strong>pull requests</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="#"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>issues, pull requests, discussions,</strong> and <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">#</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="@"
              data-scope-types="[&quot;&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>organizations, repositories,</strong> and <strong>users</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">@</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="!"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>projects</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">!</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="/"
              data-scope-types="[&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Search for <strong>files</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">/</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="modes_help"
              data-prefix="&gt;"
          >
            <span data-target="command-palette-help.titleElement">Activate <strong>command mode</strong></span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd">&gt;</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# author:@me"
          >
            <span data-target="command-palette-help.titleElement">Search your issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># author:@me</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:pr"
          >
            <span data-target="command-palette-help.titleElement">Filter to pull requests</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:pr</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:issue"
          >
            <span data-target="command-palette-help.titleElement">Filter to issues</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:issue</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:discussion"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:discussion</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:project"
              data-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          >
            <span data-target="command-palette-help.titleElement">Filter to projects</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:project</kbd>
              </span>
          </command-palette-help>
          <command-palette-help
            data-group="filters_help"
              data-prefix="# is:open"
          >
            <span data-target="command-palette-help.titleElement">Filter to open issues, pull requests, and discussions</span>
              <span data-target="command-palette-help.hintElement">
                <kbd class="hx_kbd"># is:open</kbd>
              </span>
          </command-palette-help>
      </server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/commands"
          data-supported-modes="[&quot;&gt;&quot;]"
            data-supports-commands
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_page_navigation"
          data-supported-modes="[&quot;&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/jump_to_members_only"
          data-supported-modes="[&quot;&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/jump_to_members_only_prefetched"
          data-supported-modes="[&quot;@&quot;,&quot;@&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;&quot;,&quot;owner&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="files"
          data-fetch-debounce="0"
            data-src="/command_palette/files"
          data-supported-modes="[&quot;/&quot;]"
            data-supported-scope-types="[&quot;repository&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/discussions"
          data-supported-modes="[&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/projects"
          data-supported-modes="[&quot;#&quot;,&quot;!&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="prefetched"
          data-fetch-debounce="0"
            data-src="/command_palette/recent_issues"
          data-supported-modes="[&quot;#&quot;,&quot;#&quot;]"
            data-supported-scope-types="[&quot;owner&quot;,&quot;repository&quot;,&quot;&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/teams"
          data-supported-modes="[&quot;@&quot;,&quot;&quot;]"
            data-supported-scope-types="[&quot;owner&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="remote"
          data-fetch-debounce="200"
            data-src="/command_palette/name_with_owner_repository"
          data-supported-modes="[&quot;&quot;]"
          
          ></server-defined-provider>
        <server-defined-provider
          data-type="main-window-commands"
          data-fetch-debounce="0"
          data-supported-modes="[&quot;&gt;&quot;]"
            data-supports-commands
          
          ></server-defined-provider>
    </command-palette>
  </details-dialog>
</details>

<div class="position-fixed bottom-0 left-0 ml-5 mb-5 js-command-palette-toasts" style="z-index: 1000">
  <div hidden class="Toast Toast--loading">
    <span class="Toast-icon">
      <svg class="Toast--spinner" viewBox="0 0 32 32" width="18" height="18" aria-hidden="true">
        <path
          fill="#959da5"
          d="M16 0 A16 16 0 0 0 16 32 A16 16 0 0 0 16 0 M16 4 A12 12 0 0 1 16 28 A12 12 0 0 1 16 4"
        />
        <path fill="#ffffff" d="M16 0 A16 16 0 0 1 32 16 L28 16 A12 12 0 0 0 16 4z"></path>
      </svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--error">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path fill-rule="evenodd" d="M4.47.22A.75.75 0 015 0h6a.75.75 0 01.53.22l4.25 4.25c.141.14.22.331.22.53v6a.75.75 0 01-.22.53l-4.25 4.25A.75.75 0 0111 16H5a.75.75 0 01-.53-.22L.22 11.53A.75.75 0 010 11V5a.75.75 0 01.22-.53L4.47.22zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5H5.31zM8 4a.75.75 0 01.75.75v3.5a.75.75 0 01-1.5 0v-3.5A.75.75 0 018 4zm0 8a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast Toast--warning">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>


  <div hidden class="anim-fade-in fast Toast Toast--success">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>

  <div hidden class="anim-fade-in fast Toast">
    <span class="Toast-icon">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm6.5-.25A.75.75 0 017.25 7h1a.75.75 0 01.75.75v2.75h.25a.75.75 0 010 1.5h-2a.75.75 0 010-1.5h.25v-2h-.25a.75.75 0 01-.75-.75zM8 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
    </span>
    <span class="Toast-content"></span>
  </div>
</div>

      <div hidden class="js-command-palette-pjax-meta-data" data-pjax-replace id="command-palette-pjax-meta-data"
    data-subject-id="MDEwOlJlcG9zaXRvcnkxNTI5OTI2NjA="
    data-subject-type="Repository"
>
</div>


  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" data-pjax-container >
      

<template class="js-user-list-create-dialog-template" data-label="Create list">
  <div class="Box-header">
    <h2 class="Box-title">Create list</h2>
  </div>
  <form class="Box-body d-flex flex-column p-3 js-user-list-form" action="/stars/phenolophthaleinum/lists" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Rwe13YzRO0ialp_bYivk19iD9rYJFVVqinDAk6tvvdTcXCAePuGiV1SpQIGCBGFxgzW1TaZFNlowF6W4sYBoCA" autocomplete="off" />
        <p class="color-fg-subtle mb-3">Create a list to organize your starred repositories.</p>
      <input type="hidden" name="repository_id" value="{{ repositoryId }}">

  <div class="form-group mx-0 mt-0 mb-2 js-user-list-input-container js-characters-remaining-container position-relative">
    <auto-check src="/stars/phenolophthaleinum/list-check?attr=name" required>
      <text-expander keys=":" data-emoji-url="/autocomplete/emoji">
        <input
          type="text"
          name="user_list[name]"
          class="form-control js-user-list-input js-characters-remaining-field"
          placeholder="⭐️ Name this list"
          value=""
          aria-label="List name"
          maxlength="32"
          data-maxlength="32"
          autofocus
          required
        >
      </text-expander>
      <input type="hidden" value="C0GgONihhVwmLIAdT7fgxso-K_fZ2hTpPanEtjptZB6i_oOIwekLq2fpEosZdUuGFhODxbNWqp-KtEj4ZU__dA" data-csrf="true" />
    </auto-check>
    <p
      class="note error position-relative js-user-list-error"
       hidden
    >
      Name .
    </p>
    <p class="mt-1 text-small float-right js-characters-remaining" data-suffix="remaining" hidden>
      32 remaining
    </p>
  </div>
  <div class="form-group mx-0 mt-0 mb-2 js-user-list-input-container js-characters-remaining-container position-relative">
    <text-expander keys=":" data-emoji-url="/autocomplete/emoji">
      <textarea
        name="user_list[description]"
        class="form-control js-user-list-input js-characters-remaining-field"
        placeholder="Write a description"
        aria-label="List description"
        maxlength="160"
        data-maxlength="160"
        style="height: 74px; min-height: 74px"
      ></textarea>
    </text-expander>
    <p
      class="note error position-relative js-user-list-error"
       hidden
    >
      Description .
    </p>
    <p class="mt-1 text-small float-right js-characters-remaining" data-suffix="remaining" hidden>
      160 remaining
    </p>
  </div>
  <div hidden="hidden" data-generic-message="Unable to save your list at this time." data-view-component="true" class="js-user-list-base flash flash-error mx-0 mt-0 mb-2">
  
  
    .


  
</div>      <button disabled="disabled" data-disable-invalid="true" data-submitting-message="Creating..." type="submit" data-view-component="true" class="btn-primary btn btn-block mt-2">  Create
</button>

  <p class="note mt-2 mb-0">
    <strong>Tip:</strong> type <code>:</code> to add emoji to the name or description.
  </p>
</form>
  <div data-view-component="true" class="Box-footer Box-row--gray text-small color-fg-muted d-flex flex-items-baseline py-2">
  <span title="Feature Release Label: Beta" aria-label="Feature Release Label: Beta" data-view-component="true" class="Label Label--success Label--inline px-2 mr-2">Beta</span>
  <span class="mr-1">Lists are currently in beta.</span>
  <a href="/github/feedback/discussions/categories/lists-feedback">Share feedback and report bugs.</a>
</div>
</template>



    






  <div id="repository-container-header" class="pt-3 hide-full-screen mb-5" style="background-color: var(--color-page-header-bg);" data-pjax-replace>

      <div class="d-flex mb-3 px-3 px-md-4 px-lg-5">

        <div class="flex-auto min-width-0 width-fit mr-3">
            <h1 class=" d-flex flex-wrap flex-items-center wb-break-word f3 text-normal">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo color-fg-muted mr-2">
    <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path>
</svg>
  <span class="author flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/rmenegaux/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/rmenegaux">rmenegaux</a>
  </span>
  <span class="mx-1 flex-self-stretch color-fg-muted">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA">fastDNA</a>
  </strong>

  <span></span><span class="Label Label--secondary v-align-middle mr-1">Public</span>
</h1>

        </div>

          <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">

  

  <li>
        <notifications-list-subscription-form
      data-action="notifications-dialog-label-toggled:notifications-list-subscription-form#handleDialogLabelToggle"
      class="f5 position-relative"
    >
      <details
        class="details-reset details-overlay f5 position-relative"
        data-target="notifications-list-subscription-form.details"
        data-action="toggle:notifications-list-subscription-form#detailsToggled"
      >

      <summary data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="edcca1a86589433aa128afdeafac1f43810414c69e23a541c3848a1bb4df84c9" data-ga-click="Repository, click Watch settings, action:files#disambiguate" aria-label="Notification settings" data-view-component="true" class="btn-sm btn">  <span data-menu-button>
            <span
              hidden
              
              data-target="notifications-list-subscription-form.unwatchButtonCopy"
            >
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Unwatch
            </span>
            <span
              hidden
              
              data-target="notifications-list-subscription-form.stopIgnoringButtonCopy"
            >
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell-slash">
    <path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path>
</svg>
              Stop ignoring
            </span>
            <span
              
              
              data-target="notifications-list-subscription-form.watchButtonCopy"
            >
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Watch
            </span>
          </span>
            <span id="repo-notifications-counter" data-target="notifications-list-subscription-form.socialCount" data-pjax-replace="true" title="4" data-view-component="true" class="Counter">4</span>
          <span class="dropdown-caret"></span>
</summary>
        <details-menu
          class="SelectMenu  "
          role="menu"
          data-target="notifications-list-subscription-form.menu"
          
        >
          <div class="SelectMenu-modal notifications-component-menu-modal">
            <header class="SelectMenu-header">
              <h3 class="SelectMenu-title">Notifications</h3>
              <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-action="click:notifications-list-subscription-form#closeMenu">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
              </button>
            </header>

            <div class="SelectMenu-list">
              <form data-target="notifications-list-subscription-form.form" data-action="submit:notifications-list-subscription-form#submitForm" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="nSp7XnjtwQJyx2QNiKkXZfIuuCucHsAgvQSh237QhUwrnaUpJ9VUtiL9EzbfU0SHVnWJqj86XazKsaWaBrpClQ" autocomplete="off" />

                <input type="hidden" name="repository_id" value="152992660">

                <button
                  type="submit"
                  name="do"
                  value="included"
                  class="SelectMenu-item flex-items-start"
                  role="menuitemradio"
                  aria-checked="true"
                  data-targets="notifications-list-subscription-form.subscriptionButtons"
                  
                >
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Participating and @mentions
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Only receive notifications from this repository when participating or @mentioned.
                    </div>
                  </div>
                </button>

                <button
                  type="submit"
                  name="do"
                  value="subscribed"
                  class="SelectMenu-item flex-items-start"
                  role="menuitemradio"
                  aria-checked="false"
                  data-targets="notifications-list-subscription-form.subscriptionButtons"
                >
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      All Activity
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Notified of all notifications on this repository.
                    </div>
                  </div>
                </button>

                <button
                  type="submit"
                  name="do"
                  value="ignore"
                  class="SelectMenu-item flex-items-start"
                  role="menuitemradio"
                  aria-checked="false"
                  data-targets="notifications-list-subscription-form.subscriptionButtons"
                >
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Ignore
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Never be notified.
                    </div>
                  </div>
                </button>
</form>
              <button
                class="SelectMenu-item flex-items-start pr-3"
                type="button"
                role="menuitemradio"
                data-target="notifications-list-subscription-form.customButton"
                data-action="click:notifications-list-subscription-form#openCustomDialog"
                aria-haspopup="true"
                aria-checked="false"
                
              >
                <span class="f5">
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                </span>
                <div>
                  <div class="d-flex flex-items-start flex-justify-between">
                    <div class="f5 text-bold">Custom</div>
                    <div class="f5 pr-1">
                      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-right">
    <path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path>
</svg>
                    </div>
                  </div>
                  <div class="text-small color-fg-muted text-normal pb-1">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </div>
              </button>

            </div>
          </div>
        </details-menu>

        <details-dialog
          class="notifications-component-dialog "
          data-target="notifications-list-subscription-form.customDialog"
          aria-label="Custom dialog"
          hidden
        >
          <div class="SelectMenu-modal notifications-component-dialog-modal overflow-visible">
            <form data-target="notifications-list-subscription-form.customform" data-action="submit:notifications-list-subscription-form#submitCustomForm" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="a0pqt6tXJtamgCrotikRD3g3f0bl4HT2eW7ColZhXE_d_bTA9G-zYva6XdPh00Lt3GxOx0bE6XoO28bjLgublg" autocomplete="off" />

              <input type="hidden" name="repository_id" value="152992660">

              <header class="d-sm-none SelectMenu-header pb-0 border-bottom-0 px-2 px-sm-3">
                <h1 class="f3 SelectMenu-title d-inline-flex">
                  <button
                    class="color-bg-default border-0 px-2 py-0 m-0 Link--secondary f5"
                    aria-label="Return to menu"
                    type="button"
                    data-action="click:notifications-list-subscription-form#closeCustomDialog"
                  >
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                  </button>
                  Custom
                </h1>
              </header>

              <header class="d-none d-sm-flex flex-items-start pt-1">
                <button
                  class="border-0 px-2 pt-1 m-0 Link--secondary f5"
                  style="background-color: transparent;"
                  aria-label="Return to menu"
                  type="button"
                  data-action="click:notifications-list-subscription-form#closeCustomDialog"
                >
                  <svg style="position: relative; left: 2px; top: 1px" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                </button>

                <h1 class="pt-1 pr-4 pb-0 pl-0 f5 text-bold">
                  Custom
                </h1>
              </header>

              <fieldset>
                <legend>
                  <div class="text-small color-fg-muted pt-0 pr-3 pb-3 pl-6 pl-sm-5 border-bottom mb-3">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </legend>
                <div data-target="notifications-list-subscription-form.labelInputs">
                </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="Issue"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Issues
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="PullRequest"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Pull requests
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="Release"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Releases
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="Discussion"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Discussions
                    </label>

                      <span
                        class="tooltipped tooltipped-nw mr-2 p-1 float-right"
                        
                        aria-label="Discussions are not enabled for this repo">
                        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info color-fg-muted">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm6.5-.25A.75.75 0 017.25 7h1a.75.75 0 01.75.75v2.75h.25a.75.75 0 010 1.5h-2a.75.75 0 010-1.5h.25v-2h-.25a.75.75 0 01-.75-.75zM8 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
                      </span>
                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="SecurityAlert"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Security alerts
                    </label>

                  </div>
              </fieldset>
              <div class="pt-2 pb-3 px-3 d-flex flex-justify-start flex-row-reverse">
                <button name="do" value="custom" data-target="notifications-list-subscription-form.customSubmit" disabled="disabled" type="submit" data-view-component="true" class="btn-primary btn-sm btn ml-2">  Apply
</button>

                <button data-action="click:notifications-list-subscription-form#resetForm" data-close-dialog="" type="button" data-view-component="true" class="btn-sm btn">  Cancel
</button>
              </div>
</form>          </div>
        </details-dialog>


        <div class="notifications-component-dialog-overlay"></div>
      </details>
    </notifications-list-subscription-form>



  </li>

  <li>
            <form class="btn-with-count" action="/rmenegaux/fastDNA/fork" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="F7aZYc0LM5oAAoqYow12V4SmJhmm5YG9aja1pF8jlnEg8pl3c1DACI_MzTVB0FuoMWveWcm13J4AyUbsyEKhrA" autocomplete="off" />
        <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="fb6d2359e926ec32c93b40768ff7711322fa0a04cefe45b9d5300656aa9b3094" data-ga-click="Repository, show fork modal, action:files#disambiguate; text:Fork" aria-label="Fork your own copy of rmenegaux/fastDNA to your account" type="submit" data-view-component="true" class="btn-sm btn">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>Fork
          <span id="repo-network-counter" data-pjax-replace="true" title="11" data-view-component="true" class="Counter">11</span>
</button></form>
  </li>

  <li>
        <template class="js-unstar-confirmation-dialog-template">
  <div class="Box-header">
    <h2 class="Box-title">Unstar this repository?</h2>
  </div>
  <div class="Box-body">
    <p class="mb-3">
      This will remove {{ repoNameWithOwner }} from the {{ listsWithCount }} that it's been added to.
    </p>
    <div class="form-actions">
      <form class="js-social-confirmation-form" action="{{ confirmUrl }}" accept-charset="UTF-8" method="post">
        <input type="hidden" name="authenticity_token" value="{{ confirmCsrfToken }}">
        <input type="hidden" name="confirm" value="true">
        <button data-close-dialog="true" type="submit" data-view-component="true" class="btn-danger btn width-full">  Unstar
</button>
</form>    </div>
  </div>
</template>

  <div data-view-component="true" class="js-toggler-container js-social-container starring-container BtnGroup d-flex">
    <form class="starred js-social-form BtnGroup-parent flex-auto js-deferred-toggler-target" action="/rmenegaux/fastDNA/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="ylvtQQLc4Ylo7HLI77_JxBJHcheXfg7kR76RXUcCgLtFPbWF8A_uxGHGdUtTrFKLRhB46MF6NrHUrxxGqLvlkg" autocomplete="off" />
        <input type="hidden" value="F9hIKoxRDFxQez6_5Gx97Nhgk8a36u3So6HpL8_gt9SYvhDufoIDEVlROTxYf-ajjDeZOeHu1YcwsGQ0IFnS_Q" data-csrf="true" class="js-confirm-csrf-token" />
      <input type="hidden" name="context" value="repository">
      <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="f0633a94a21b1e4119bb9db3c8946cd8c704ad7bf91e8359d227cdb4671379a3" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar" aria-label="Unstar this repository" type="submit" data-view-component="true" class="rounded-left-2 border-right-0 btn-sm btn BtnGroup-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill starred-button-icon d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"></path>
</svg><span data-view-component="true" class="d-inline">
          Starred
</span>          <span id="repo-stars-counter-unstar" aria-label="18 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-pjax-replace="true" title="18" data-view-component="true" class="Counter js-social-count">18</span>
</button></form>
    <form class="unstarred js-social-form BtnGroup-parent flex-auto" action="/rmenegaux/fastDNA/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="JVqnZFFeg9o3LqQg8RzBSZHJt7E0z21lZ4jXr2PiRe2mDbBFoBhihAhsMxUrgF_f7yfulytKDIYKkD6gZsvhAg" autocomplete="off" />
      <input type="hidden" name="context" value="repository">
      <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="e995dc0665707adce425032bce38469cbcf9bd4ec590c7f97753c808f355a57b" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star" aria-label="Star this repository" type="submit" data-view-component="true" class="js-toggler-target rounded-left-2 btn-sm btn BtnGroup-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>          <span id="repo-stars-counter-star" aria-label="18 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-pjax-replace="true" title="18" data-view-component="true" class="Counter js-social-count">18</span>
</button></form>
      <details id="details-e2da7b" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-inline-block position-relative">
      <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
</summary>
  <details-menu
    class="SelectMenu right-0"
      src="/rmenegaux/fastDNA/lists"
      
      role="menu"
      
>
    <div class="SelectMenu-modal">
        <button class="SelectMenu-closeButton position-absolute right-0 m-2" type="button" aria-label="Close menu" data-toggle-for="details-e2da7b">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      <div
        id="filter-menu-e2da7b"
        class="d-flex flex-column flex-1 overflow-hidden"
>
        <div
          class="SelectMenu-list"
          >

            <include-fragment class="SelectMenu-loading" aria-label="Loading">
              <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
            </include-fragment>
        </div>
        
      </div>
    </div>
  </details-menu>
</details>
</div>
  </li>

  

</ul>

      </div>

      <div id="responsive-meta-container" data-pjax-replace>
      <div class="d-block d-md-none mb-2 px-3 px-md-4 px-lg-5">
      <div class="mb-2">
        <a href="/rmenegaux/fastDNA/blob/master/LICENSE" class="Link--muted">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-law mr-1">
    <path fill-rule="evenodd" d="M8.75.75a.75.75 0 00-1.5 0V2h-.984c-.305 0-.604.08-.869.23l-1.288.737A.25.25 0 013.984 3H1.75a.75.75 0 000 1.5h.428L.066 9.192a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.514 3.514 0 00.686.45A4.492 4.492 0 003 11c.88 0 1.556-.22 2.023-.454a3.515 3.515 0 00.686-.45l.045-.04.016-.015.006-.006.002-.002.001-.002L5.25 9.5l.53.53a.75.75 0 00.154-.838L3.822 4.5h.162c.305 0 .604-.08.869-.23l1.289-.737a.25.25 0 01.124-.033h.984V13h-2.5a.75.75 0 000 1.5h6.5a.75.75 0 000-1.5h-2.5V3.5h.984a.25.25 0 01.124.033l1.29.736c.264.152.563.231.868.231h.162l-2.112 4.692a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.517 3.517 0 00.686.45A4.492 4.492 0 0013 11c.88 0 1.556-.22 2.023-.454a3.512 3.512 0 00.686-.45l.045-.04.01-.01.006-.005.006-.006.002-.002.001-.002-.529-.531.53.53a.75.75 0 00.154-.838L13.823 4.5h.427a.75.75 0 000-1.5h-2.234a.25.25 0 01-.124-.033l-1.29-.736A1.75 1.75 0 009.735 2H8.75V.75zM1.695 9.227c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327l-1.305 2.9zm10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327l-1.305 2.9z"></path>
</svg>
            View license
        </a>
      </div>
    <div class="mb-3">
      <a class="Link--secondary no-underline mr-3" href="/rmenegaux/fastDNA/stargazers">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
        <span class="text-bold">18</span>
        stars
</a>      <a class="Link--secondary no-underline" href="/rmenegaux/fastDNA/network/members">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-1">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
        <span class="text-bold">11</span>
        forks
</a>    </div>
    <div class="d-flex">
      <div class="flex-1 mr-2">
          <template class="js-unstar-confirmation-dialog-template">
  <div class="Box-header">
    <h2 class="Box-title">Unstar this repository?</h2>
  </div>
  <div class="Box-body">
    <p class="mb-3">
      This will remove {{ repoNameWithOwner }} from the {{ listsWithCount }} that it's been added to.
    </p>
    <div class="form-actions">
      <form class="js-social-confirmation-form" action="{{ confirmUrl }}" accept-charset="UTF-8" method="post">
        <input type="hidden" name="authenticity_token" value="{{ confirmCsrfToken }}">
        <input type="hidden" name="confirm" value="true">
        <button data-close-dialog="true" type="submit" data-view-component="true" class="btn-danger btn width-full">  Unstar
</button>
</form>    </div>
  </div>
</template>

  <div data-view-component="true" class="js-toggler-container js-social-container starring-container BtnGroup d-flex">
    <form class="starred js-social-form BtnGroup-parent flex-auto js-deferred-toggler-target" action="/rmenegaux/fastDNA/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="wqpuZdFd2qc7Tii7Q8aQ9ovv9QzrZAaJE4ate8_cZWNNzDahI47V6jJkLzj_1Qu537j_871gPtyAlyBgIGUASg" autocomplete="off" />
        <input type="hidden" value="F2FEF6jTVTYp9HrURN43ECGonZ2fVskUtQ7w1XRwjJaYBxzTWgBaeyDefVf4zaxfdf-XYslS8UEmH33Om8npvw" data-csrf="true" class="js-confirm-csrf-token" />
      <input type="hidden" name="context" value="repository">
      <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="f0633a94a21b1e4119bb9db3c8946cd8c704ad7bf91e8359d227cdb4671379a3" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar" aria-label="Unstar this repository" type="submit" data-view-component="true" class="rounded-left-2 border-right-0 btn-sm btn btn-block BtnGroup-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill starred-button-icon d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"></path>
</svg><span data-view-component="true" class="d-inline">
          Starred
</span>
</button></form>
    <form class="unstarred js-social-form BtnGroup-parent flex-auto" action="/rmenegaux/fastDNA/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="fNX2Ba-EOwxHHamo4JDXEQjxyzLPOTh00Egd5ngc4Dr_guEkXsLaUnhfPp06DEmHdh-SFNC8WZe9UPTpfTVE1Q" autocomplete="off" />
      <input type="hidden" name="context" value="repository">
      <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="e995dc0665707adce425032bce38469cbcf9bd4ec590c7f97753c808f355a57b" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star" aria-label="Star this repository" type="submit" data-view-component="true" class="js-toggler-target rounded-left-2 btn-sm btn btn-block BtnGroup-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star d-inline-block mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg><span data-view-component="true" class="d-inline">
          Star
</span>
</button></form>
      <details id="details-2a884e" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-inline-block position-relative">
      <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="M4.427 7.427l3.396 3.396a.25.25 0 00.354 0l3.396-3.396A.25.25 0 0011.396 7H4.604a.25.25 0 00-.177.427z"></path>
</svg>
</summary>
  <details-menu
    class="SelectMenu right-0"
      src="/rmenegaux/fastDNA/lists"
      
      role="menu"
      
>
    <div class="SelectMenu-modal">
        <button class="SelectMenu-closeButton position-absolute right-0 m-2" type="button" aria-label="Close menu" data-toggle-for="details-2a884e">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      <div
        id="filter-menu-2a884e"
        class="d-flex flex-column flex-1 overflow-hidden"
>
        <div
          class="SelectMenu-list"
          >

            <include-fragment class="SelectMenu-loading" aria-label="Loading">
              <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
            </include-fragment>
        </div>
        
      </div>
    </div>
  </details-menu>
</details>
</div>
      </div>
      <div class="flex-1">
            <notifications-list-subscription-form
      data-action="notifications-dialog-label-toggled:notifications-list-subscription-form#handleDialogLabelToggle"
      class="f5 position-relative"
    >
      <details
        class="details-reset details-overlay f5 position-relative"
        data-target="notifications-list-subscription-form.details"
        data-action="toggle:notifications-list-subscription-form#detailsToggled"
      >

      <summary data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="edcca1a86589433aa128afdeafac1f43810414c69e23a541c3848a1bb4df84c9" data-ga-click="Repository, click Watch settings, action:files#disambiguate" aria-label="Notification settings" data-view-component="true" class="btn-sm btn btn-block">  <span data-menu-button>
            <span
              hidden
              
              data-target="notifications-list-subscription-form.unwatchButtonCopy"
            >
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Unwatch
            </span>
            <span
              hidden
              
              data-target="notifications-list-subscription-form.stopIgnoringButtonCopy"
            >
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell-slash">
    <path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path>
</svg>
              Stop ignoring
            </span>
            <span
              
              
              data-target="notifications-list-subscription-form.watchButtonCopy"
            >
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
              Watch
            </span>
          </span>
          <span class="dropdown-caret"></span>
</summary>
        <details-menu
          class="SelectMenu  "
          role="menu"
          data-target="notifications-list-subscription-form.menu"
          
        >
          <div class="SelectMenu-modal notifications-component-menu-modal">
            <header class="SelectMenu-header">
              <h3 class="SelectMenu-title">Notifications</h3>
              <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-action="click:notifications-list-subscription-form#closeMenu">
                <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
              </button>
            </header>

            <div class="SelectMenu-list">
              <form data-target="notifications-list-subscription-form.form" data-action="submit:notifications-list-subscription-form#submitForm" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="BsyDyt5Vwe_sTr-xIObr1PEDh86vJmqYfUvhGvZOEWKwe129gW1UW7x0yIp3HLg2VVi2TwwC9xQK_uVbjiTWuw" autocomplete="off" />

                <input type="hidden" name="repository_id" value="152992660">

                <button
                  type="submit"
                  name="do"
                  value="included"
                  class="SelectMenu-item flex-items-start"
                  role="menuitemradio"
                  aria-checked="true"
                  data-targets="notifications-list-subscription-form.subscriptionButtons"
                  
                >
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Participating and @mentions
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Only receive notifications from this repository when participating or @mentioned.
                    </div>
                  </div>
                </button>

                <button
                  type="submit"
                  name="do"
                  value="subscribed"
                  class="SelectMenu-item flex-items-start"
                  role="menuitemradio"
                  aria-checked="false"
                  data-targets="notifications-list-subscription-form.subscriptionButtons"
                >
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      All Activity
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Notified of all notifications on this repository.
                    </div>
                  </div>
                </button>

                <button
                  type="submit"
                  name="do"
                  value="ignore"
                  class="SelectMenu-item flex-items-start"
                  role="menuitemradio"
                  aria-checked="false"
                  data-targets="notifications-list-subscription-form.subscriptionButtons"
                >
                  <span class="f5">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                  </span>
                  <div>
                    <div class="f5 text-bold">
                      Ignore
                    </div>
                    <div class="text-small color-fg-muted text-normal pb-1">
                      Never be notified.
                    </div>
                  </div>
                </button>
</form>
              <button
                class="SelectMenu-item flex-items-start pr-3"
                type="button"
                role="menuitemradio"
                data-target="notifications-list-subscription-form.customButton"
                data-action="click:notifications-list-subscription-form#openCustomDialog"
                aria-haspopup="true"
                aria-checked="false"
                
              >
                <span class="f5">
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
                </span>
                <div>
                  <div class="d-flex flex-items-start flex-justify-between">
                    <div class="f5 text-bold">Custom</div>
                    <div class="f5 pr-1">
                      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-right">
    <path fill-rule="evenodd" d="M8.22 2.97a.75.75 0 011.06 0l4.25 4.25a.75.75 0 010 1.06l-4.25 4.25a.75.75 0 01-1.06-1.06l2.97-2.97H3.75a.75.75 0 010-1.5h7.44L8.22 4.03a.75.75 0 010-1.06z"></path>
</svg>
                    </div>
                  </div>
                  <div class="text-small color-fg-muted text-normal pb-1">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </div>
              </button>

            </div>
          </div>
        </details-menu>

        <details-dialog
          class="notifications-component-dialog "
          data-target="notifications-list-subscription-form.customDialog"
          aria-label="Custom dialog"
          hidden
        >
          <div class="SelectMenu-modal notifications-component-dialog-modal overflow-visible">
            <form data-target="notifications-list-subscription-form.customform" data-action="submit:notifications-list-subscription-form#submitCustomForm" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="HAUefNcXXzMPKo7sRtey-jLJZvDDomJQl87KODPsvBOqssALiC_Kh18Q-dcRLeEYlpJXcWCG_9zge855S4Z7yg" autocomplete="off" />

              <input type="hidden" name="repository_id" value="152992660">

              <header class="d-sm-none SelectMenu-header pb-0 border-bottom-0 px-2 px-sm-3">
                <h1 class="f3 SelectMenu-title d-inline-flex">
                  <button
                    class="color-bg-default border-0 px-2 py-0 m-0 Link--secondary f5"
                    aria-label="Return to menu"
                    type="button"
                    data-action="click:notifications-list-subscription-form#closeCustomDialog"
                  >
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                  </button>
                  Custom
                </h1>
              </header>

              <header class="d-none d-sm-flex flex-items-start pt-1">
                <button
                  class="border-0 px-2 pt-1 m-0 Link--secondary f5"
                  style="background-color: transparent;"
                  aria-label="Return to menu"
                  type="button"
                  data-action="click:notifications-list-subscription-form#closeCustomDialog"
                >
                  <svg style="position: relative; left: 2px; top: 1px" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-arrow-left">
    <path fill-rule="evenodd" d="M7.78 12.53a.75.75 0 01-1.06 0L2.47 8.28a.75.75 0 010-1.06l4.25-4.25a.75.75 0 011.06 1.06L4.81 7h7.44a.75.75 0 010 1.5H4.81l2.97 2.97a.75.75 0 010 1.06z"></path>
</svg>
                </button>

                <h1 class="pt-1 pr-4 pb-0 pl-0 f5 text-bold">
                  Custom
                </h1>
              </header>

              <fieldset>
                <legend>
                  <div class="text-small color-fg-muted pt-0 pr-3 pb-3 pl-6 pl-sm-5 border-bottom mb-3">
                    Select events you want to be notified of in addition to participating and @mentions.
                  </div>
                </legend>
                <div data-target="notifications-list-subscription-form.labelInputs">
                </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="Issue"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Issues
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="PullRequest"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Pull requests
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="Release"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Releases
                    </label>

                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="Discussion"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Discussions
                    </label>

                      <span
                        class="tooltipped tooltipped-nw mr-2 p-1 float-right"
                        
                        aria-label="Discussions are not enabled for this repo">
                        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-info color-fg-muted">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm6.5-.25A.75.75 0 017.25 7h1a.75.75 0 01.75.75v2.75h.25a.75.75 0 010 1.5h-2a.75.75 0 010-1.5h.25v-2h-.25a.75.75 0 01-.75-.75zM8 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
                      </span>
                  </div>
                  <div class="form-checkbox mr-3 ml-6 ml-sm-5 mb-2 mt-0">
                    <label class="f5 text-normal">
                      <input
                        type="checkbox"
                        name="thread_types[]"
                        value="SecurityAlert"
                        data-targets="notifications-list-subscription-form.threadTypeCheckboxes"
                        data-action="change:notifications-list-subscription-form#threadTypeCheckboxesUpdated"
                        
                      >
                      Security alerts
                    </label>

                  </div>
              </fieldset>
              <div class="pt-2 pb-3 px-3 d-flex flex-justify-start flex-row-reverse">
                <button name="do" value="custom" data-target="notifications-list-subscription-form.customSubmit" disabled="disabled" type="submit" data-view-component="true" class="btn-primary btn-sm btn ml-2">  Apply
</button>

                <button data-action="click:notifications-list-subscription-form#resetForm" data-close-dialog="" type="button" data-view-component="true" class="btn-sm btn">  Cancel
</button>
              </div>
</form>          </div>
        </details-dialog>


        <div class="notifications-component-dialog-overlay"></div>
      </details>
    </notifications-list-subscription-form>



      </div>
    </div>
  </div>

</div>


        
<nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="/rmenegaux/fastDNA" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /rmenegaux/fastDNA" data-pjax="#repo-content-pjax-container" data-hotkey="g c" data-ga-click="Repository, Navigation click, Code tab" aria-current="page" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path>
</svg>
          <span data-content="Code">Code</span>
            <span id="code-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="/rmenegaux/fastDNA/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /rmenegaux/fastDNA/issues" data-pjax="#repo-content-pjax-container" data-hotkey="g i" data-ga-click="Repository, Navigation click, Issues tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path><path fill-rule="evenodd" d="M8 0a8 8 0 100 16A8 8 0 008 0zM1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0z"></path>
</svg>
          <span data-content="Issues">Issues</span>
            <span id="issues-repo-tab-count" data-pjax-replace="" title="3" data-view-component="true" class="Counter">3</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="/rmenegaux/fastDNA/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /rmenegaux/fastDNA/pulls" data-pjax="#repo-content-pjax-container" data-hotkey="g p" data-ga-click="Repository, Navigation click, Pull requests tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path>
</svg>
          <span data-content="Pull requests">Pull requests</span>
            <span id="pull-requests-repo-tab-count" data-pjax-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="/rmenegaux/fastDNA/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /rmenegaux/fastDNA/actions" data-pjax="#repo-content-pjax-container" data-hotkey="g a" data-ga-click="Repository, Navigation click, Actions tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path>
</svg>
          <span data-content="Actions">Actions</span>
            <span id="actions-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="/rmenegaux/fastDNA/projects?type=beta" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /rmenegaux/fastDNA/projects?type=beta" data-pjax="#repo-content-pjax-container" data-hotkey="g b" data-ga-click="Repository, Navigation click, Projects tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v3.585a.746.746 0 010 .83v8.085A1.75 1.75 0 0114.25 16H6.309a.748.748 0 01-1.118 0H1.75A1.75 1.75 0 010 14.25V6.165a.746.746 0 010-.83V1.75zM1.5 6.5v7.75c0 .138.112.25.25.25H5v-8H1.5zM5 5H1.5V1.75a.25.25 0 01.25-.25H5V5zm1.5 1.5v8h7.75a.25.25 0 00.25-.25V6.5h-8zm8-1.5h-8V1.5h7.75a.25.25 0 01.25.25V5z"></path>
</svg>
          <span data-content="Projects">Projects</span>
            <span id="projects-repo-tab-count" data-pjax-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="wiki-tab" href="/rmenegaux/fastDNA/wiki" data-tab-item="i5wiki-tab" data-selected-links="repo_wiki /rmenegaux/fastDNA/wiki" data-pjax="#repo-content-pjax-container" data-hotkey="g w" data-ga-click="Repository, Navigation click, Wikis tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z"></path>
</svg>
          <span data-content="Wiki">Wiki</span>
            <span id="wiki-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="/rmenegaux/fastDNA/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /rmenegaux/fastDNA/security" data-pjax="#repo-content-pjax-container" data-hotkey="g s" data-ga-click="Repository, Navigation click, Security tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z"></path>
</svg>
          <span data-content="Security">Security</span>
            <include-fragment src="/rmenegaux/fastDNA/security/overall-count" accept="text/fragment+html"></include-fragment>

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="/rmenegaux/fastDNA/pulse" data-tab-item="i7insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /rmenegaux/fastDNA/pulse" data-pjax="#repo-content-pjax-container" data-ga-click="Repository, Navigation click, Insights tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path>
</svg>
          <span data-content="Insights">Insights</span>
            <span id="insights-repo-tab-count" data-pjax-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <details data-view-component="true" class="details-overlay details-reset position-relative">
  <summary role="button" data-view-component="true">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
  <div data-view-component="true">          <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw">
  
            <ul>
                <li data-menu-item="i0code-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item selected dropdown-item" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /rmenegaux/fastDNA" href="/rmenegaux/fastDNA">
                    Code
</a>                </li>
                <li data-menu-item="i1issues-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_issues repo_labels repo_milestones /rmenegaux/fastDNA/issues" href="/rmenegaux/fastDNA/issues">
                    Issues
</a>                </li>
                <li data-menu-item="i2pull-requests-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /rmenegaux/fastDNA/pulls" href="/rmenegaux/fastDNA/pulls">
                    Pull requests
</a>                </li>
                <li data-menu-item="i3actions-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /rmenegaux/fastDNA/actions" href="/rmenegaux/fastDNA/actions">
                    Actions
</a>                </li>
                <li data-menu-item="i4projects-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_projects new_repo_project repo_project /rmenegaux/fastDNA/projects?type=beta" href="/rmenegaux/fastDNA/projects?type=beta">
                    Projects
</a>                </li>
                <li data-menu-item="i5wiki-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_wiki /rmenegaux/fastDNA/wiki" href="/rmenegaux/fastDNA/wiki">
                    Wiki
</a>                </li>
                <li data-menu-item="i6security-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /rmenegaux/fastDNA/security" href="/rmenegaux/fastDNA/security">
                    Security
</a>                </li>
                <li data-menu-item="i7insights-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /rmenegaux/fastDNA/pulse" href="/rmenegaux/fastDNA/pulse">
                    Insights
</a>                </li>
            </ul>

</details-menu></div>
</details></div>
</nav>
  </div>



<div class="clearfix new-discussion-timeline container-xl px-3 px-md-4 px-lg-5">
  <div id="repo-content-pjax-container" class="repository-content " >

      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank">Open in a new github.dev tab</a>



    
      
  

<div>
  

  <div class="d-none d-lg-block mt-6 mr-3 Popover top-0 right-0 color-shadow-medium col-3">
    
  </div>

  <div id="spoof-warning" class="mt-0 pb-3" hidden aria-hidden>
  <div data-view-component="true" class="flash flash-warn mt-0 clearfix">
  
  
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert float-left mt-1">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>

      <div class="overflow-hidden">This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.</div>


  
</div></div>

  <include-fragment src="/rmenegaux/fastDNA/spoofed_commit_check/bc6469694daa69a18c458166ef4975b9fc1c308c" data-test-selector="spoofed-commit-check"></include-fragment>

  <div data-view-component="true" class="Layout Layout--flowRow-until-md Layout--sidebarPosition-end Layout--sidebarPosition-flowRow-end">
  <div data-view-component="true" class="Layout-main">      
      
        <include-fragment src="/rmenegaux/fastDNA/show_partial?partial=tree%2Frecently_touched_branches_list"></include-fragment>
      <div class="file-navigation mb-3 d-flex flex-items-start">
  
<div class="position-relative">
  <details class="details-reset details-overlay mr-0 mb-0 " id="branch-select-menu">
    <summary class="btn css-truncate"
            data-hotkey="w"
            title="Switch branches or tags">
      <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path>
</svg>
      <span class="css-truncate-target" data-menu-button>master</span>
      <span class="dropdown-caret"></span>
    </summary>

      
<div class="SelectMenu">
  <div class="SelectMenu-modal">
    <header class="SelectMenu-header">
      <span class="SelectMenu-title">Switch branches/tags</span>
      <button class="SelectMenu-closeButton" type="button" data-toggle-for="branch-select-menu"><svg aria-label="Close menu" aria-hidden="false" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg></button>
    </header>

    <input-demux data-action="tab-container-change:input-demux#storeInput tab-container-changed:input-demux#updateInput">
      <tab-container class="d-flex flex-column js-branches-tags-tabs" style="min-height: 0;">
        <div class="SelectMenu-filter">
          <input data-target="input-demux.source"
                 id="context-commitish-filter-field"
                 class="SelectMenu-input form-control"
                 aria-owns="ref-list-branches"
                 data-controls-ref-menu-id="ref-list-branches"
                 autofocus
                 autocomplete="off"
                 aria-label="Filter branches/tags"
                 placeholder="Filter branches/tags"
                 type="text"
          >
        </div>

        <div class="SelectMenu-tabs" role="tablist" data-target="input-demux.control" >
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="true">Branches</button>
          <button class="SelectMenu-tab" type="button" role="tab">Tags</button>
        </div>

        <div role="tabpanel" id="ref-list-branches" data-filter-placeholder="Filter branches/tags" tabindex="" class="d-flex flex-column flex-auto overflow-auto">
          <ref-selector
            type="branch"
            data-targets="input-demux.sinks"
            data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            "
            query-endpoint="/rmenegaux/fastDNA/refs"
            
            cache-key="v0:1601913339.0"
            current-committish="bWFzdGVy"
            default-branch="bWFzdGVy"
            name-with-owner="cm1lbmVnYXV4L2Zhc3RETkE="
            prefetch-on-mouseover
          >

            <template data-target="ref-selector.fetchFailedTemplate">
              <div class="SelectMenu-message" data-index="{{ index }}">Could not load branches</div>
            </template>

              <template data-target="ref-selector.noMatchTemplate">
    <div class="SelectMenu-message">Nothing to show</div>
</template>


            <!-- TODO: this max-height is necessary or else the branch list won't scroll.  why? -->
            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list " style="max-height: 330px" data-pjax="#repo-content-pjax-container">
              <div class="SelectMenu-loading pt-3 pb-0 overflow-hidden" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
              </div>
            </div>

              <template data-target="ref-selector.itemTemplate">
  <a href="https://github.com/rmenegaux/fastDNA/tree/{{ urlEncodedRefName }}" class="SelectMenu-item" role="menuitemradio" rel="nofollow" aria-checked="{{ isCurrent }}" data-index="{{ index }}">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    <span class="flex-1 css-truncate css-truncate-overflow {{ isFilteringClass }}">{{ refName }}</span>
    <span hidden="{{ isNotDefault }}" class="Label Label--secondary flex-self-start">default</span>
  </a>
</template>


              <footer class="SelectMenu-footer"><a href="/rmenegaux/fastDNA/branches">View all branches</a></footer>
          </ref-selector>

        </div>

        <div role="tabpanel" id="tags-menu" data-filter-placeholder="Find a tag" tabindex="" hidden class="d-flex flex-column flex-auto overflow-auto">
          <ref-selector
            type="tag"
            data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            "
            data-targets="input-demux.sinks"
            query-endpoint="/rmenegaux/fastDNA/refs"
            cache-key="v0:1601913339.0"
            current-committish="bWFzdGVy"
            default-branch="bWFzdGVy"
            name-with-owner="cm1lbmVnYXV4L2Zhc3RETkE="
          >

            <template data-target="ref-selector.fetchFailedTemplate">
              <div class="SelectMenu-message" data-index="{{ index }}">Could not load tags</div>
            </template>

            <template data-target="ref-selector.noMatchTemplate">
              <div class="SelectMenu-message" data-index="{{ index }}">Nothing to show</div>
            </template>

              <template data-target="ref-selector.itemTemplate">
  <a href="https://github.com/rmenegaux/fastDNA/tree/{{ urlEncodedRefName }}" class="SelectMenu-item" role="menuitemradio" rel="nofollow" aria-checked="{{ isCurrent }}" data-index="{{ index }}">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    <span class="flex-1 css-truncate css-truncate-overflow {{ isFilteringClass }}">{{ refName }}</span>
    <span hidden="{{ isNotDefault }}" class="Label Label--secondary flex-self-start">default</span>
  </a>
</template>


            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list" style="max-height: 330px" data-pjax="#repo-content-pjax-container">
              <div class="SelectMenu-loading pt-3 pb-0 overflow-hidden" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" />
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" />
</svg>
              </div>
            </div>
              <footer class="SelectMenu-footer"><a href="/rmenegaux/fastDNA/tags">View all tags</a></footer>
          </ref-selector>
        </div>
      </tab-container>
    </input-demux>
  </div>
</div>

  </details>

</div>


  <div class="flex-self-center ml-3 flex-self-stretch d-none d-lg-flex flex-items-center lh-condensed-ultra">
    <a data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/branches" class="Link--primary no-underline">
          <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path>
</svg>
          <strong>8</strong>
          <span class="color-fg-muted">branches</span>
    </a>
    <a data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/tags" class="ml-3 Link--primary no-underline">
      <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag">
    <path fill-rule="evenodd" d="M2.5 7.775V2.75a.25.25 0 01.25-.25h5.025a.25.25 0 01.177.073l6.25 6.25a.25.25 0 010 .354l-5.025 5.025a.25.25 0 01-.354 0l-6.25-6.25a.25.25 0 01-.073-.177zm-1.5 0V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 010 2.474l-5.026 5.026a1.75 1.75 0 01-2.474 0l-6.25-6.25A1.75 1.75 0 011 7.775zM6 5a1 1 0 100 2 1 1 0 000-2z"></path>
</svg>
        <strong>0</strong>
        <span class="color-fg-muted">tags</span>
    </a>
  </div>

  <div class="flex-auto"></div>

  <include-fragment data-test-selector="overview-actions-fragment" src="/rmenegaux/fastDNA/overview_actions/master"></include-fragment>


    <span class="d-none d-md-flex ml-2">
      
<get-repo class="">
    <feature-callout class="feature-callout"
                   data-query-path="/settings/notice-dismissals/codespaces_code_tab"
                   data-feature-name="codespaces_code_tab"
  >
    
    <details class="position-relative details-overlay details-reset js-codespaces-details-container"
             data-action="toggle:get-repo#onDetailsToggle"
             
    >
      <summary data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:152992660,&quot;target&quot;:&quot;CLONE_OR_DOWNLOAD_BUTTON&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="6c28fa9f1ad2d756a7157072d5629f14b799a970502598acc27254a40fa7cbb2" data-view-component="true" class="btn-primary btn">  Code<span class="dropdown-caret"></span>
</summary>      <div class="position-relative">
        <div class="dropdown-menu dropdown-menu-sw p-0" style="top:6px;width:378px;">
            <div
  data-target="get-repo.modal"
  
>
    <ul class="list-style-none">
        <li class="Box-row p-3">
  <a class="Link--muted float-right tooltipped tooltipped-s" href="https://docs.github.com/articles/which-remote-url-should-i-use" target="_blank" aria-label="Which remote URL should I use?">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-question">
    <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path>
</svg>
</a>

<div class="text-bold">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-terminal mr-2">
    <path fill-rule="evenodd" d="M0 2.75C0 1.784.784 1 1.75 1h12.5c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0114.25 15H1.75A1.75 1.75 0 010 13.25V2.75zm1.75-.25a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25V2.75a.25.25 0 00-.25-.25H1.75zM7.25 8a.75.75 0 01-.22.53l-2.25 2.25a.75.75 0 11-1.06-1.06L5.44 8 3.72 6.28a.75.75 0 111.06-1.06l2.25 2.25c.141.14.22.331.22.53zm1.5 1.5a.75.75 0 000 1.5h3a.75.75 0 000-1.5h-3z"></path>
</svg>
  Clone
</div>

<tab-container>

  <div class="UnderlineNav my-2 box-shadow-none">
    <div class="UnderlineNav-body" role="tablist">
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" action="/users/set_protocol?protocol_type=clone" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="-bHSKrNlvTwrPbbcI1eDyF4Ma5vYeAnYaIMO3_NBJdsVyhaaLSk4p0JARHHbJBS4b7G2t7Quqh0r2OlHarGgaA" />
            <button name="protocol_selector" type="submit" role="tab" class="UnderlineNav-item lh-default f6 py-0 px-0 mr-2 position-relative" aria-selected="true" value="http" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_HTTPS&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="caefae00816c80a9e5c4bb411cb37f26b7858fa5f6c2a029aeb78c70c1f17424">
              HTTPS
</button></form>          <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" action="/users/set_protocol?protocol_type=clone" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="PCrelCw1ejWEnSO2-pCpBvWZwdgO1GUt4YWGHoJ8GQDQURoksnn_ru3g0RsC4z52xCQc9GKCxuii3mGGG4ycsw" />
            <button name="protocol_selector" type="submit" role="tab" class="UnderlineNav-item lh-default f6 py-0 px-0 mr-2 position-relative" value="ssh" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_SSH&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="722be4f4e3aedd19238dd8b0331c840b56c3930a26e4b1b0b1a21bcd8b572221">
              SSH
</button></form>          <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" action="/users/set_protocol?protocol_type=clone" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="nKVbfwBf0LImzx3jGHIvmbVqV9SntYrL1vZZLEq70ABw3p_PnhNVKU-y707gAbjphNeK-MvjKQ6Vrb6000tVsw" />
            <button name="protocol_selector" type="submit" role="tab" class="UnderlineNav-item lh-default f6 py-0 px-0 mr-2 position-relative" value="gh_cli" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;USE_GH_CLI&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="e953bbd914c6240ea628790a5c59d66c788c6fb8b2eaca5f2da10e89a3e61b8c">
              GitHub CLI
</button></form>    </div>
  </div>

  <div role="tabpanel">
    <div class="input-group">
  <input type="text" class="form-control input-monospace input-sm color-bg-subtle" data-autoselect value="https://github.com/rmenegaux/fastDNA.git" aria-label="https://github.com/rmenegaux/fastDNA.git" readonly>
  <div class="input-group-button">
    <clipboard-copy value="https://github.com/rmenegaux/fastDNA.git" aria-label="Copy to clipboard" class="btn btn-sm js-clipboard-copy tooltipped-no-delay ClipboardButton js-clone-url-http" data-copy-feedback="Copied!" data-tooltip-direction="n" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="368e39805f544911079ca463f07e7cbcd21444a17c4c3f698ec8bd994407b211"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon d-inline-block">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-inline-block d-sm-none">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg></clipboard-copy>
  </div>
</div>

    <p class="mt-2 mb-0 f6 color-fg-muted">
        Use Git or checkout with SVN using the web URL.
    </p>
  </div>

  <div role="tabpanel" hidden>
      <div data-view-component="true" class="f6 flash flash-warn mt-2 mb-3 p-3">
  
  
        You don't have any public SSH keys in your GitHub account.
        You can <a href="/settings/ssh/new">add a new public key</a>, or try cloning this repository via HTTPS.


  
</div>
    <div class="input-group">
  <input type="text" class="form-control input-monospace input-sm color-bg-subtle" data-autoselect value="git@github.com:rmenegaux/fastDNA.git" aria-label="git@github.com:rmenegaux/fastDNA.git" readonly>
  <div class="input-group-button">
    <clipboard-copy value="git@github.com:rmenegaux/fastDNA.git" aria-label="Copy to clipboard" class="btn btn-sm js-clipboard-copy tooltipped-no-delay ClipboardButton js-clone-url-ssh" data-copy-feedback="Copied!" data-tooltip-direction="n" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="368e39805f544911079ca463f07e7cbcd21444a17c4c3f698ec8bd994407b211"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon d-inline-block">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-inline-block d-sm-none">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg></clipboard-copy>
  </div>
</div>

    <p class="mt-2 mb-0 f6 color-fg-muted">
        Use a password-protected SSH key.
    </p>
  </div>

  <div role="tabpanel" hidden>
    <div class="input-group">
  <input type="text" class="form-control input-monospace input-sm color-bg-subtle" data-autoselect value="gh repo clone rmenegaux/fastDNA" aria-label="gh repo clone rmenegaux/fastDNA" readonly>
  <div class="input-group-button">
    <clipboard-copy value="gh repo clone rmenegaux/fastDNA" aria-label="Copy to clipboard" class="btn btn-sm js-clipboard-copy tooltipped-no-delay ClipboardButton js-clone-url-gh-cli" data-copy-feedback="Copied!" data-tooltip-direction="n" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;COPY_URL&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="368e39805f544911079ca463f07e7cbcd21444a17c4c3f698ec8bd994407b211"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon d-inline-block">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-inline-block d-sm-none">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg></clipboard-copy>
  </div>
</div>

    <p class="mt-2 mb-0 f6 color-fg-muted">
      Work fast with our official CLI.
      <a href="https://cli.github.com" target="_blank">Learn more</a>.
    </p>
  </div>
</tab-container>

</li>
<li data-platforms="windows,mac" class="Box-row Box-row--hover-gray p-3 mt-0 rounded-0 js-remove-unless-platform">
  <a class="d-flex flex-items-center color-fg-default text-bold no-underline" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;OPEN_IN_DESKTOP&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="945914238244efee9caed3ce85797b2ed398ec5d1cd982287f8949fa7fd26b2f" data-action="click:get-repo#showDownloadMessage" href="x-github-client://openRepo/https://github.com/rmenegaux/fastDNA">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-desktop-download mr-2">
    <path d="M4.927 5.427l2.896 2.896a.25.25 0 00.354 0l2.896-2.896A.25.25 0 0010.896 5H8.75V.75a.75.75 0 10-1.5 0V5H5.104a.25.25 0 00-.177.427z"></path><path d="M1.573 2.573a.25.25 0 00-.073.177v7.5a.25.25 0 00.25.25h12.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-3a.75.75 0 110-1.5h3A1.75 1.75 0 0116 2.75v7.5A1.75 1.75 0 0114.25 12h-3.727c.099 1.041.52 1.872 1.292 2.757A.75.75 0 0111.25 16h-6.5a.75.75 0 01-.565-1.243c.772-.885 1.192-1.716 1.292-2.757H1.75A1.75 1.75 0 010 10.25v-7.5A1.75 1.75 0 011.75 1h3a.75.75 0 010 1.5h-3a.25.25 0 00-.177.073zM6.982 12a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5H6.982z"></path>
</svg>
    Open with GitHub Desktop
</a></li>
  <li data-platforms="windows,mac" class="Box-row Box-row--hover-gray p-3 mt-0 js-remove-unless-platform">
    <a class="d-flex flex-items-center color-fg-default text-bold no-underline" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;OPEN_IN_VISUAL_STUDIO&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="097c30415dd4a0b7ca34e21199b438e508034d14a8c89789b855c958448558d5" data-open-app="visual-studio" data-action="click:get-repo#showDownloadMessage" href="git-client://clone?repo=https%3A%2F%2Fgithub.com%2Frmenegaux%2FfastDNA">
      Open with Visual Studio
</a>  </li>
<li class="Box-row Box-row--hover-gray p-3 mt-0" >
  <a class="d-flex flex-items-center color-fg-default text-bold no-underline" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;clone_or_download.click&quot;,&quot;payload&quot;:{&quot;feature_clicked&quot;:&quot;DOWNLOAD_ZIP&quot;,&quot;git_repository_type&quot;:&quot;REPOSITORY&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="f3849cd0db239de06b92d0855f69d315bafc98d288a93086c97e62013443dcc2" data-ga-click="Repository, download zip, location:repo overview" data-open-app="link" href="/rmenegaux/fastDNA/archive/refs/heads/master.zip">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-zip mr-2">
    <path fill-rule="evenodd" d="M3.5 1.75a.25.25 0 01.25-.25h3a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h2.086a.25.25 0 01.177.073l2.914 2.914a.25.25 0 01.073.177v8.586a.25.25 0 01-.25.25h-.5a.75.75 0 000 1.5h.5A1.75 1.75 0 0014 13.25V4.664c0-.464-.184-.909-.513-1.237L10.573.513A1.75 1.75 0 009.336 0H3.75A1.75 1.75 0 002 1.75v11.5c0 .649.353 1.214.874 1.515a.75.75 0 10.752-1.298.25.25 0 01-.126-.217V1.75zM8.75 3a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5zM6 5.25a.75.75 0 01.75-.75h.5a.75.75 0 010 1.5h-.5A.75.75 0 016 5.25zm2 1.5A.75.75 0 018.75 6h.5a.75.75 0 010 1.5h-.5A.75.75 0 018 6.75zm-1.25.75a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5zM8 9.75A.75.75 0 018.75 9h.5a.75.75 0 010 1.5h-.5A.75.75 0 018 9.75zm-.75.75a1.75 1.75 0 00-1.75 1.75v3c0 .414.336.75.75.75h2.5a.75.75 0 00.75-.75v-3a1.75 1.75 0 00-1.75-1.75h-.5zM7 12.25a.25.25 0 01.25-.25h.5a.25.25 0 01.25.25v2.25H7v-2.25z"></path>
</svg>
    Download ZIP
</a></li>

    </ul>
</div>


<div class="p-3" data-targets="get-repo.platforms" data-platform="mac" hidden>
  <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="AnimatedEllipsis"></span></h4>
  <p class="color-fg-muted">
    If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.
  </p>
  <button data-action="click:get-repo#onDetailsToggle" type="button" data-view-component="true" class="btn-link">
</button>
</div>
<div class="p-3" data-targets="get-repo.platforms" data-platform="windows" hidden>
  <h4 class="lh-condensed mb-3">Launching GitHub Desktop<span class="AnimatedEllipsis"></span></h4>
  <p class="color-fg-muted">
    If nothing happens, <a href="https://desktop.github.com/">download GitHub Desktop</a> and try again.
  </p>
  <button data-action="click:get-repo#onDetailsToggle" type="button" data-view-component="true" class="btn-link">
</button>
</div>
<div class="p-3" data-targets="get-repo.platforms" data-platform="xcode" hidden>
  <h4 class="lh-condensed mb-3">Launching Xcode<span class="AnimatedEllipsis"></span></h4>
  <p class="color-fg-muted">
    If nothing happens, <a href="https://developer.apple.com/xcode/">download Xcode</a> and try again.
  </p>
  <button data-action="click:get-repo#onDetailsToggle" type="button" data-view-component="true" class="btn-link">
</button>
</div>
<div class="p-3 " data-targets="get-repo.platforms" data-target="new-codespace.loadingVscode prefetch-pane.loadingVscode" data-platform="vscode" hidden>
  <poll-include-fragment data-target="get-repo.vscodePoller new-codespace.vscodePoller prefetch-pane.vscodePoller">
    <h4 class="lh-condensed mb-3">Launching Visual Studio Code<span class="AnimatedEllipsis" data-hide-on-error></span></h4>
    <p class="color-fg-muted" data-hide-on-error>Your codespace will open once ready.</p>
    <p class="color-fg-muted" data-show-on-error hidden>There was a problem preparing your codespace, please try again.</p>
  </poll-include-fragment>
</div>


        </div>
      </div>
    </details>

    <form class="d-none" data-target="feature-callout.dismissalForm" action="/settings/dismiss-notice/codespaces_code_tab" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="bXp3ulpCPkg_ZZrNDYkQVQapBoDR88icGprCJLeSPbOHazshYFQhbRYEUBrHQ8G3_sqe7AyC9I7LhWXcWukRDA" autocomplete="off" /></form>
  </feature-callout>
</get-repo>

        
    </span>
</div>

      


<div class="Box mb-3">
  <div class="Box-header position-relative">
    <h2 class="sr-only">Latest commit</h2>
    <div class="js-details-container Details d-flex rounded-top-2 flex-items-center flex-wrap" data-issue-and-pr-hovercards-enabled>
      <include-fragment src="/rmenegaux/fastDNA/tree-commit/bc6469694daa69a18c458166ef4975b9fc1c308c" class="d-flex flex-auto flex-items-center" aria-busy="true" aria-label="Loading latest commit">
        <div class="Skeleton avatar avatar-user flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1" style="width:24px;height:24px;"></div>
        <div class="Skeleton Skeleton--text col-5 ml-3">&nbsp;</div>
</include-fragment>      <div class="flex-shrink-0">
        <h2 class="sr-only">Git stats</h2>
        <ul class="list-style-none d-flex">
          <li class="ml-0 ml-md-3">
            <a data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/commits/master" class="pl-3 pr-3 py-3 p-md-0 mt-n3 mb-n3 mr-n3 m-md-0 Link--primary no-underline no-wrap">
              <svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-history">
    <path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"></path>
</svg>
              <span class="d-none d-sm-inline">
                    <strong>18</strong>
                    <span aria-label="Commits on master" class="color-fg-muted d-none d-lg-inline">
                      commits
                    </span>
              </span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
    <h2 id="files"  class="sr-only">Files</h2>
    


  <include-fragment src="/rmenegaux/fastDNA/file-list/master">
      <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/rmenegaux/fastDNA/tree/bc6469694daa69a18c458166ef4975b9fc1c308c">Permalink</a>

  <div data-view-component="true" class="include-fragment-error flash flash-error flash-full py-2">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
  
    Failed to load latest commit information.


  
</div>  <div class="js-details-container Details">
    <div role="grid" aria-labelledby="files" class="Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block" data-pjax>
      <div class="sr-only" role="row">
        <div role="columnheader">Type</div>
        <div role="columnheader">Name</div>
        <div role="columnheader" class="d-none d-md-block">Latest commit message</div>
        <div role="columnheader">Commit time</div>
      </div>

        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory hx_color-icon-directory">
    <path fill-rule="evenodd" d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3h-6.5a.25.25 0 01-.2-.1l-.9-1.2c-.33-.44-.85-.7-1.4-.7h-3.5z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="This path skips through empty directories" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/tree/master/python/fastDNA"><span class="color-fg-muted">python/</span>fastDNA</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory hx_color-icon-directory">
    <path fill-rule="evenodd" d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3h-6.5a.25.25 0 01-.2-.1l-.9-1.2c-.33-.44-.85-.7-1.4-.7h-3.5z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="src" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/tree/master/src">src</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory hx_color-icon-directory">
    <path fill-rule="evenodd" d="M1.75 1A1.75 1.75 0 000 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0016 13.25v-8.5A1.75 1.75 0 0014.25 3h-6.5a.25.25 0 01-.2-.1l-.9-1.2c-.33-.44-.85-.7-1.4-.7h-3.5z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="test" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/tree/master/test">test</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title=".gitignore" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/blob/master/.gitignore">.gitignore</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="LICENSE" data-pjax="#repo-content-pjax-container" itemprop="license" href="/rmenegaux/fastDNA/blob/master/LICENSE">LICENSE</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="MANIFEST.in" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/blob/master/MANIFEST.in">MANIFEST.in</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="Makefile" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/blob/master/Makefile">Makefile</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="PATENTS" data-pjax="#repo-content-pjax-container" itemprop="license" href="/rmenegaux/fastDNA/blob/master/PATENTS">PATENTS</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="README.md" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/blob/master/README.md">README.md</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="fdna.py" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/blob/master/fdna.py">fdna.py</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
        <div role="row" class="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item ">
          <div role="gridcell" class="mr-3 flex-shrink-0" style="width: 16px;">
              <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <path fill-rule="evenodd" d="M3.75 1.5a.25.25 0 00-.25.25v11.5c0 .138.112.25.25.25h8.5a.25.25 0 00.25-.25V6H9.75A1.75 1.75 0 018 4.25V1.5H3.75zm5.75.56v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237v8.086A1.75 1.75 0 0112.25 15h-8.5A1.75 1.75 0 012 13.25V1.75z"></path>
</svg>
          </div>

          <div role="rowheader" class="flex-auto min-width-0 col-md-2 mr-3">
            <span class="css-truncate css-truncate-target d-block width-fit"><a class="js-navigation-open Link--primary" title="setup.cfg" data-pjax="#repo-content-pjax-container" href="/rmenegaux/fastDNA/blob/master/setup.cfg">setup.cfg</a></span>
          </div>

          <div role="gridcell" class="flex-auto min-width-0 d-none d-md-block col-5 mr-3" >
              <div class="Skeleton Skeleton--text col-7">&nbsp;</div>
          </div>

          <div role="gridcell" class="color-fg-muted text-right" style="width:100px;">
              <div class="Skeleton Skeleton--text">&nbsp;</div>
          </div>

        </div>
    </div>
    <div class="Details-content--shown Box-footer d-md-none p-0">
      <button aria-expanded="false" type="button" data-view-component="true" class="js-details-target btn-link d-block width-full px-3 py-2">  View code
</button>    </div>
  </div>

</include-fragment>


</div>

    <readme-toc>

    <div id="readme" class="Box md js-code-block-container js-code-nav-container js-tagsearch-file Box--responsive"
        data-tagsearch-path="README.md"
        data-tagsearch-lang="Markdown">

      <div class="d-flex  js-sticky js-position-sticky top-0 border-top-0 border-bottom p-2 flex-items-center flex-justify-between color-bg-default rounded-top-2"  style="position: sticky; z-index: 30;" >
        <div class="d-flex flex-items-center">
            <details
  data-target="readme-toc.trigger"
  data-menu-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;trigger&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}"
  data-menu-hydro-click-hmac="b4e4c002984ef46809077b692170d28c9cff203e6a1fd86b004c6bea5c5ccbef"
  class="dropdown details-reset details-overlay"
>
  <summary
    class="btn btn-octicon m-0 mr-2 p-2"
    aria-haspopup="true"
    aria-label="Table of Contents">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-unordered">
    <path fill-rule="evenodd" d="M2 4a1 1 0 100-2 1 1 0 000 2zm3.75-1.5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zm0 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zm0 5a.75.75 0 000 1.5h8.5a.75.75 0 000-1.5h-8.5zM3 8a1 1 0 11-2 0 1 1 0 012 0zm-1 6a1 1 0 100-2 1 1 0 000 2z"></path>
</svg>
  </summary>


  <details-menu class="SelectMenu" role="menu">
    <div class="SelectMenu-modal rounded-3 mt-1" style="max-height:340px;">

        <div class="SelectMenu-filter">
          <input
            class="SelectMenu-input form-control js-filterable-field"
            id="toc-filter-field"
            type="text"
            autocomplete="off"
            spellcheck="false"
            autofocus
            placeholder="Filter headings"
            aria-label="Filter headings">
        </div>

      <div class="SelectMenu-list SelectMenu-list--borderless p-2" style="overscroll-behavior: contain;" data-filterable-for="toc-filter-field" data-filterable-type="substring">
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#table-of-contents">Table of contents</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#introduction">Introduction</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#requirements">Requirements</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#building-fastdna">Building fastDNA</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#dna-short-read-classification">DNA short read classification</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#full-documentation">Full documentation</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#python">Python</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#data">Data</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 text-emphasized" style="-webkit-box-orient: vertical; padding-left: 12px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#the-data-used-in-the-paper-is-available-here-httpprojectscbiomines-paristechfrlargescalemetagenomics">The data used in the paper is available here: http://projects.cbio.mines-paristech.fr/largescalemetagenomics/.</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#references">References</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#continuous-embedding-of-dna-reads-and-application-to-metagenomics">Continuous Embedding of DNA reads, and application to metagenomics</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#enriching-word-vectors-with-subword-information">Enriching Word Vectors with Subword Information</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#bag-of-tricks-for-efficient-text-classification">Bag of Tricks for Efficient Text Classification</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#fasttextzip-compressing-text-classification-models">FastText.zip: Compressing text classification models</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:152992660,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8e2f9ec74bfc69e853f8333cf87efd9b726ce52ae714b7d7502d8a87d09d6492" href="#license">License</a>
      </div>
    </div>
  </details-menu>
</details>

          <h2 class="Box-title">
            <a href="#readme" data-view-component="true" class="Link--primary">README.md</a>
          </h2>
        </div>
      </div>

          <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/rmenegaux/fastDNA/find-definition"
     data-tagsearch-ref="master"
     data-tagsearch-code-nav-context="BLOB_VIEW">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box color-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>

        <div data-target="readme-toc.content" class="Box-body px-5 pb-5">
          <article class="markdown-body entry-content container-lg" itemprop="text"><h2 dir="auto"><a id="user-content-table-of-contents" class="anchor" aria-hidden="true" href="#table-of-contents"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Table of contents</h2>
<ul dir="auto">
<li><a href="#introduction">Introduction</a></li>
<li><a href="#requirements">Requirements</a></li>
<li><a href="#building-fastdna">Building fastDNA</a></li>
<li><a href="#command-line-interface">Command line interface</a>
<ul dir="auto">
<li><a href="#full-documentation">Full documentation</a></li>
</ul>
</li>
<li><a href="#python">Python</a></li>
<li><a href="#data">Data</a></li>
<li><a href="#references">References</a>
<ul dir="auto">
<li><a href="#continuous-embedding-of-dna-reads-and-application-to-metagenomics">Continuous Embedding of DNA reads and application to metagenomics</a></li>
<li><a href="#enriching-word-vectors-with-subword-information">Enriching Word Vectors with Subword Information</a></li>
<li><a href="#bag-of-tricks-for-efficient-text-classification">Bag of Tricks for Efficient Text Classification</a></li>
<li><a href="#fasttextzip-compressing-text-classification-models">FastText.zip: Compressing text classification models</a></li>
</ul>
</li>
<li><a href="#license">License</a></li>
</ul>
<h2 dir="auto"><a id="user-content-introduction" class="anchor" aria-hidden="true" href="#introduction"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introduction</h2>
<p dir="auto"><a href="#continuous-embedding-of-dna-reads-and-application-to-metagenomics">fastDNA</a> is a library for classification of short DNA sequences.
It is adapted from the <a href="https://fasttext.cc/" rel="nofollow">fastText</a> library.</p>
<h2 dir="auto"><a id="user-content-requirements" class="anchor" aria-hidden="true" href="#requirements"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Requirements</h2>
<p dir="auto">Generally, <strong>fastText</strong> builds on modern Mac OS and Linux distributions.
Since it uses some C++11 features, it requires a compiler with good C++11 support.
These include :</p>
<ul dir="auto">
<li>(g++-4.7.2 or newer) or (clang-3.3 or newer)</li>
</ul>
<p dir="auto">Compilation is carried out using a Makefile, so you will need to have a working <strong>make</strong>.</p>
<h2 dir="auto"><a id="user-content-building-fastdna" class="anchor" aria-hidden="true" href="#building-fastdna"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Building fastDNA</h2>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ git clone https://github.com/rmenegaux/fastDNA.git
$ cd fastDNA
$ make"><pre><code>$ git clone https://github.com/rmenegaux/fastDNA.git
$ cd fastDNA
$ make
</code></pre></div>
<p dir="auto">This will produce object files for all the classes as well as the main binary <code>fastdna</code>.</p>
<p dir="auto">For a trial run:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ cd test
$ sh test.sh"><pre><code>$ cd test
$ sh test.sh
</code></pre></div>
<p dir="auto">This should train and evaluate a small model on the toy dataset provided.</p>
<h3 dir="auto"><a id="user-content-dna-short-read-classification" class="anchor" aria-hidden="true" href="#dna-short-read-classification"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>DNA short read classification</h3>
<p dir="auto">In order to train a dna classifier using the method described in <a href="#continuous-embedding-of-dna-reads-and-application-to-metagenomics">1</a>, use:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna supervised -input train.fasta -labels labels.txt -output model"><pre><code>$ ./fastdna supervised -input train.fasta -labels labels.txt -output model
</code></pre></div>
<p dir="auto">where <code>train.fasta</code> is a FASTA file containing the full reference genomes and <code>labels.txt</code> is a text file containing the genome labels (one label per line).
This will output two files: <code>model.bin</code> and <code>model.vec</code>.</p>
<p dir="auto">Once the model was trained, you can evaluate it by computing the precision and recall at k (P@k and R@k) on a test set using:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna test model.bin test.fasta test_labels.txt n"><pre><code>$ ./fastdna test model.bin test.fasta test_labels.txt n
</code></pre></div>
<p dir="auto">where <code>test.fasta</code> is a FASTA file containing the DNA fragments to be classified, and <code>test_labels.txt</code> contains the labels for each of the fragments.</p>
<p dir="auto">The argument <code>n</code> is optional, and is equal to <code>1</code> by default.</p>
<p dir="auto">In order to obtain the n most likely labels for a set of reads, use:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna predict model.bin test.fasta n"><pre><code>$ ./fastdna predict model.bin test.fasta n
</code></pre></div>
<p dir="auto">or use <code>predict-prob</code> to also get the probability for each label</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna predict-prob model.bin test.fasta n"><pre><code>$ ./fastdna predict-prob model.bin test.fasta n
</code></pre></div>
<p dir="auto">Doing so will print to the standard output the n most likely labels for each line.
The argument <code>n</code> is optional, and equal to <code>1</code> by default.</p>
<p dir="auto">If you want to compute vector representations of DNA sequences, please use:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna print-word-vectors model.bin &lt; text.fasta"><pre><code>$ ./fastdna print-word-vectors model.bin &lt; text.fasta
</code></pre></div>
<p dir="auto">This assumes that the <code>text.fasta</code> file contains the DNA sequences that you want to get vectors for.
The program will output one vector representation per sequence in the file.</p>
<p dir="auto">To write the vectors to a file, redirect the output as so:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna print-word-vectors model.bin &lt; text.fasta &gt; vectors.txt"><pre><code>$ ./fastdna print-word-vectors model.bin &lt; text.fasta &gt; vectors.txt
</code></pre></div>
<p dir="auto">To get vectors from standard input, just type</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna print-word-vectors model.bin"><pre><code>$ ./fastdna print-word-vectors model.bin
</code></pre></div>
<p dir="auto">Press Enter, then type the sequence and finish with Ctrl+D (Linux, Mac) or Ctrl+Z (Windows)</p>
<p dir="auto">You can also quantize a supervised model to reduce its memory usage with the following command:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna quantize -output model"><pre><code>$ ./fastdna quantize -output model
</code></pre></div>
<p dir="auto">This will create a <code>.ftz</code> file with a smaller memory footprint. All the standard functionality, like <code>test</code> or <code>predict</code> work the same way on the quantized models:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna test model.ftz test.fasta test_labels.txt"><pre><code>$ ./fastdna test model.ftz test.fasta test_labels.txt
</code></pre></div>
<p dir="auto">The quantization procedure follows the steps described in <a href="#fasttextzip-compressing-text-classification-models">3</a>.</p>
<h3 dir="auto"><a id="user-content-full-documentation" class="anchor" aria-hidden="true" href="#full-documentation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Full documentation</h3>
<p dir="auto">Invoke a command without arguments to list available arguments and their default values:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="$ ./fastdna supervised
Empty input or output path.

The following arguments are mandatory:
  -input              training file path
  -output             output file path

The following arguments are optional:
  -verbose            verbosity level [2]

The following arguments for the dictionary are optional:
  -minn               min length of char ngram [0]
  -maxn               max length of char ngram [0]
  -label              labels prefix [__label__]

The following arguments for training are optional:
  -lr                 learning rate [0.1]
  -lrUpdateRate       change the rate of updates for the learning rate [100]
  -dim                size of word vectors [100]
  -noise              mutation rate (/100,000)[0]
  -length             length of fragments for training [200]
  -epoch              number of epochs [5]
  -loss               loss function {ns, hs, softmax} [softmax]
  -thread             number of threads [12]
  -pretrainedVectors  pretrained word vectors for supervised learning []
  -loadModel          pretrained model for supervised learning []
  -saveOutput         whether output params should be saved [false]
  -freezeEmbeddings   model does not update the embedding vectors [false]

The following arguments for quantization are optional:
  -cutoff             number of words and ngrams to retain [0]
  -retrain            whether embeddings are finetuned if a cutoff is applied [false]
  -qnorm              whether the norm is quantized separately [false]
  -qout               whether the classifier is quantized [false]
  -dsub               size of each sub-vector [2]"><pre><code>$ ./fastdna supervised
Empty input or output path.

The following arguments are mandatory:
  -input              training file path
  -output             output file path

The following arguments are optional:
  -verbose            verbosity level [2]

The following arguments for the dictionary are optional:
  -minn               min length of char ngram [0]
  -maxn               max length of char ngram [0]
  -label              labels prefix [__label__]

The following arguments for training are optional:
  -lr                 learning rate [0.1]
  -lrUpdateRate       change the rate of updates for the learning rate [100]
  -dim                size of word vectors [100]
  -noise              mutation rate (/100,000)[0]
  -length             length of fragments for training [200]
  -epoch              number of epochs [5]
  -loss               loss function {ns, hs, softmax} [softmax]
  -thread             number of threads [12]
  -pretrainedVectors  pretrained word vectors for supervised learning []
  -loadModel          pretrained model for supervised learning []
  -saveOutput         whether output params should be saved [false]
  -freezeEmbeddings   model does not update the embedding vectors [false]

The following arguments for quantization are optional:
  -cutoff             number of words and ngrams to retain [0]
  -retrain            whether embeddings are finetuned if a cutoff is applied [false]
  -qnorm              whether the norm is quantized separately [false]
  -qout               whether the classifier is quantized [false]
  -dsub               size of each sub-vector [2]
</code></pre></div>
<h2 dir="auto"><a id="user-content-python" class="anchor" aria-hidden="true" href="#python"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Python</h2>
<p dir="auto">Most use cases are covered in the python script <code>fdna.py</code>.</p>
<p dir="auto">To reproduce the results from the paper, download the <a href="#data">data</a> then run:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="python fdna.py -train -train_fasta /path/to/train_large_fasta -train_labels /path/to/train_large_labels \
    -eval -test_fasta /path/to/test_large_fasta -test_labels /path/to/test_large_labels \
    -k 13 -d 100 -noise 4 -e 200"><pre><code>python fdna.py -train -train_fasta /path/to/train_large_fasta -train_labels /path/to/train_large_labels \
    -eval -test_fasta /path/to/test_large_fasta -test_labels /path/to/test_large_labels \
    -k 13 -d 100 -noise 4 -e 200
</code></pre></div>
<p dir="auto">NB: Best parameters for classification tasks are <code>k=14, d=50, noise=4</code></p>
<p dir="auto">Full usage:</p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="python fdna.py --help
usage: fdna.py [-h] [-train] [-quantize] [-predict] [-eval] [-predict_quant]
               [-train_fasta TRAIN_FASTA] [-train_labels TRAIN_LABELS]
               [-test_fasta TEST_FASTA] [-test_labels TEST_LABELS]
               [-output_dir OUTPUT_DIR] [-model_name MODEL_NAME]
               [-threads THREADS] [-d D] [-k K] [-e E] [-lr LR] [-noise NOISE]
               [-L L] [-freeze] [-pretrained_vectors PRETRAINED_VECTORS]
               [-verbose VERBOSE]

train, predict and/or quantize fdna model

optional arguments:
  -h, --help            show this help message and exit
  -train                train model
  -quantize             quantize model
  -predict              make predictions
  -eval                 make and evaluate predictions
  -predict_quant        make and evaluate predictions with quantized model
  -train_fasta TRAIN_FASTA
                        training dataset, fasta file containing full genomes
  -train_labels TRAIN_LABELS
                        training labels, text file containing as many labels
                        as there are training genomes
  -test_fasta TEST_FASTA
                        testing dataset, fasta file containing reads
  -test_labels TEST_LABELS
                        testing dataset, text file containing as many labels
                        as there are reads
  -output_dir OUTPUT_DIR
                        output directory
  -model_name MODEL_NAME
                        optional user-defined model name
  -threads THREADS      number of threads
  -d D                  embedding dimension
  -k K                  k-mer length
  -e E                  number of training epochs
  -lr LR                learning rate
  -noise NOISE          level of training noise, percent of random mutations
  -L L                  training read length
  -freeze               freeze the embeddings
  -pretrained_vectors PRETRAINED_VECTORS
                        pretrained vectors .vec files
  -verbose VERBOSE      output verbosity, 0 1 or 2"><pre><code>python fdna.py --help
usage: fdna.py [-h] [-train] [-quantize] [-predict] [-eval] [-predict_quant]
               [-train_fasta TRAIN_FASTA] [-train_labels TRAIN_LABELS]
               [-test_fasta TEST_FASTA] [-test_labels TEST_LABELS]
               [-output_dir OUTPUT_DIR] [-model_name MODEL_NAME]
               [-threads THREADS] [-d D] [-k K] [-e E] [-lr LR] [-noise NOISE]
               [-L L] [-freeze] [-pretrained_vectors PRETRAINED_VECTORS]
               [-verbose VERBOSE]

train, predict and/or quantize fdna model

optional arguments:
  -h, --help            show this help message and exit
  -train                train model
  -quantize             quantize model
  -predict              make predictions
  -eval                 make and evaluate predictions
  -predict_quant        make and evaluate predictions with quantized model
  -train_fasta TRAIN_FASTA
                        training dataset, fasta file containing full genomes
  -train_labels TRAIN_LABELS
                        training labels, text file containing as many labels
                        as there are training genomes
  -test_fasta TEST_FASTA
                        testing dataset, fasta file containing reads
  -test_labels TEST_LABELS
                        testing dataset, text file containing as many labels
                        as there are reads
  -output_dir OUTPUT_DIR
                        output directory
  -model_name MODEL_NAME
                        optional user-defined model name
  -threads THREADS      number of threads
  -d D                  embedding dimension
  -k K                  k-mer length
  -e E                  number of training epochs
  -lr LR                learning rate
  -noise NOISE          level of training noise, percent of random mutations
  -L L                  training read length
  -freeze               freeze the embeddings
  -pretrained_vectors PRETRAINED_VECTORS
                        pretrained vectors .vec files
  -verbose VERBOSE      output verbosity, 0 1 or 2
</code></pre></div>
<p dir="auto">The python scripts require <code>numpy</code> and <code>scikit-learn</code> for evaluating predictions.</p>
<h2 dir="auto"><a id="user-content-data" class="anchor" aria-hidden="true" href="#data"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Data</h2>
<h1 dir="auto"><a id="user-content-the-data-used-in-the-paper-is-available-here-httpprojectscbiomines-paristechfrlargescalemetagenomics" class="anchor" aria-hidden="true" href="#the-data-used-in-the-paper-is-available-here-httpprojectscbiomines-paristechfrlargescalemetagenomics"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>The data used in the paper is available here: <a href="http://projects.cbio.mines-paristech.fr/largescalemetagenomics/" rel="nofollow">http://projects.cbio.mines-paristech.fr/largescalemetagenomics/</a>.</h1>
<p dir="auto">The <em>small</em> and <em>large</em> datasets used in the paper can be found <a href="http://projects.cbio.mines-paristech.fr/largescalemetagenomics/" rel="nofollow">here</a></p>
<h2 dir="auto"><a id="user-content-references" class="anchor" aria-hidden="true" href="#references"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>References</h2>
<h3 dir="auto"><a id="user-content-continuous-embedding-of-dna-reads-and-application-to-metagenomics" class="anchor" aria-hidden="true" href="#continuous-embedding-of-dna-reads-and-application-to-metagenomics"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Continuous Embedding of DNA reads, and application to metagenomics</h3>
<p dir="auto">[1] R. Menegaux, J. Vert, <a href="https://www.biorxiv.org/content/early/2018/05/31/335943" rel="nofollow"><em>Continuous Embedding of DNA reads, and application to metagenomics</em></a></p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="@article{menegaux2018continuous,
  title={Continuous Embedding of DNA reads and application to metagenomics},
  author={Menegaux, Romain and Vert, Jean-Philippe},
  journal={bioRxiv preprint 335943},
  year={2018}
}"><pre><code>@article{menegaux2018continuous,
  title={Continuous Embedding of DNA reads and application to metagenomics},
  author={Menegaux, Romain and Vert, Jean-Philippe},
  journal={bioRxiv preprint 335943},
  year={2018}
}
</code></pre></div>
<h3 dir="auto"><a id="user-content-enriching-word-vectors-with-subword-information" class="anchor" aria-hidden="true" href="#enriching-word-vectors-with-subword-information"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Enriching Word Vectors with Subword Information</h3>
<p dir="auto">[2] P. Bojanowski, E. Grave, A. Joulin, T. Mikolov, <a href="https://arxiv.org/abs/1607.04606" rel="nofollow"><em>Enriching Word Vectors with Subword Information</em></a></p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="@article{bojanowski2016enriching,
  title={Enriching Word Vectors with Subword Information},
  author={Bojanowski, Piotr and Grave, Edouard and Joulin, Armand and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.04606},
  year={2016}
}"><pre><code>@article{bojanowski2016enriching,
  title={Enriching Word Vectors with Subword Information},
  author={Bojanowski, Piotr and Grave, Edouard and Joulin, Armand and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.04606},
  year={2016}
}
</code></pre></div>
<h3 dir="auto"><a id="user-content-bag-of-tricks-for-efficient-text-classification" class="anchor" aria-hidden="true" href="#bag-of-tricks-for-efficient-text-classification"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Bag of Tricks for Efficient Text Classification</h3>
<p dir="auto">[3] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, <a href="https://arxiv.org/abs/1607.01759" rel="nofollow"><em>Bag of Tricks for Efficient Text Classification</em></a></p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="@article{joulin2016bag,
  title={Bag of Tricks for Efficient Text Classification},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.01759},
  year={2016}
}"><pre><code>@article{joulin2016bag,
  title={Bag of Tricks for Efficient Text Classification},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.01759},
  year={2016}
}
</code></pre></div>
<h3 dir="auto"><a id="user-content-fasttextzip-compressing-text-classification-models" class="anchor" aria-hidden="true" href="#fasttextzip-compressing-text-classification-models"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>FastText.zip: Compressing text classification models</h3>
<p dir="auto">[4] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, <a href="https://arxiv.org/abs/1612.03651" rel="nofollow"><em>FastText.zip: Compressing text classification models</em></a></p>
<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="@article{joulin2016fasttext,
  title={FastText.zip: Compressing text classification models},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Douze, Matthijs and J{\'e}gou, H{\'e}rve and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1612.03651},
  year={2016}
}"><pre><code>@article{joulin2016fasttext,
  title={FastText.zip: Compressing text classification models},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Douze, Matthijs and J{\'e}gou, H{\'e}rve and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1612.03651},
  year={2016}
}
</code></pre></div>
<ul dir="auto">
<li>Contact: <a href="mailto:romain.menegaux@mines-paristech.fr">romain.menegaux@mines-paristech.fr</a></li>
</ul>
<h2 dir="auto"><a id="user-content-license" class="anchor" aria-hidden="true" href="#license"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>License</h2>
<p dir="auto">fastText is BSD-licensed. An additional patent grant is also provided</p>
</article>
        </div>
    </div>

  </readme-toc>


</div>
  <div data-view-component="true" class="Layout-sidebar">      

      <div class="BorderGrid BorderGrid--spacious" data-pjax>
        <div class="BorderGrid-row hide-sm hide-md">
          <div class="BorderGrid-cell">
            <h2 class="mb-3 h4">About</h2>

    <div class="f4 my-3 color-fg-muted text-italic">
      No description, website, or topics provided.
    </div>


  <h3 class="sr-only">Resources</h3>
  <div class="mt-2">
    <a class="Link--muted" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="fb6e1e0c3054ebd97b5860fceb53cf38be9a8483a4079c9a2a5fed8c0198c55d" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;}" href="#readme">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book mr-2">
    <path fill-rule="evenodd" d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z"></path>
</svg>
      Readme
</a>  </div>

  <h3 class="sr-only">License</h3>
  <div class="mt-2">
    <a href="/rmenegaux/fastDNA/blob/master/LICENSE"
      class="Link--muted"
      
      data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:license&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="be3f44cd3fd997e543f318f970f4698d9c45f00aee73612ec4bc12369f369a91" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:license&quot;}"
    >
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-law mr-2">
    <path fill-rule="evenodd" d="M8.75.75a.75.75 0 00-1.5 0V2h-.984c-.305 0-.604.08-.869.23l-1.288.737A.25.25 0 013.984 3H1.75a.75.75 0 000 1.5h.428L.066 9.192a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.514 3.514 0 00.686.45A4.492 4.492 0 003 11c.88 0 1.556-.22 2.023-.454a3.515 3.515 0 00.686-.45l.045-.04.016-.015.006-.006.002-.002.001-.002L5.25 9.5l.53.53a.75.75 0 00.154-.838L3.822 4.5h.162c.305 0 .604-.08.869-.23l1.289-.737a.25.25 0 01.124-.033h.984V13h-2.5a.75.75 0 000 1.5h6.5a.75.75 0 000-1.5h-2.5V3.5h.984a.25.25 0 01.124.033l1.29.736c.264.152.563.231.868.231h.162l-2.112 4.692a.75.75 0 00.154.838l.53-.53-.53.53v.001l.002.002.002.002.006.006.016.015.045.04a3.517 3.517 0 00.686.45A4.492 4.492 0 0013 11c.88 0 1.556-.22 2.023-.454a3.512 3.512 0 00.686-.45l.045-.04.01-.01.006-.005.006-.006.002-.002.001-.002-.529-.531.53.53a.75.75 0 00.154-.838L13.823 4.5h.427a.75.75 0 000-1.5h-2.234a.25.25 0 01-.124-.033l-1.29-.736A1.75 1.75 0 009.735 2H8.75V.75zM1.695 9.227c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L3 6.327l-1.305 2.9zm10 0c.285.135.718.273 1.305.273s1.02-.138 1.305-.273L13 6.327l-1.305 2.9z"></path>
</svg>
        View license
    </a>
  </div>


<include-fragment  aria-label="Loading..." src="/rmenegaux/fastDNA/hovercards/citation/sidebar_partial?tree_name=master">
</include-fragment>

<h3 class="sr-only">Stars</h3>
<div class="mt-2">
  <a href="/rmenegaux/fastDNA/stargazers" data-view-component="true" class="Link--muted">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-2">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
    <strong>18</strong>
    stars
</a></div>

<h3 class="sr-only">Watchers</h3>
<div class="mt-2">
  <a href="/rmenegaux/fastDNA/watchers" data-view-component="true" class="Link--muted">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-2">
    <path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path>
</svg>
    <strong>4</strong>
    watching
</a></div>

<h3 class="sr-only">Forks</h3>
<div class="mt-2">
  <a href="/rmenegaux/fastDNA/network/members" data-view-component="true" class="Link--muted">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
    <strong>11</strong>
    forks
</a></div>

          </div>
        </div>
          <div class="BorderGrid-row">
            <div class="BorderGrid-cell">
              <h2 class="h4 mb-3" data-pjax="#repo-content-pjax-container">
  <a href="/rmenegaux/fastDNA/releases" data-view-component="true" class="Link--primary no-underline">
    Releases
</a></h2>

    <div class="text-small color-fg-muted">No releases published</div>

            </div>
          </div>
          <div class="BorderGrid-row">
            <div class="BorderGrid-cell">
              <h2 class="h4 mb-3">
  <a href="/users/rmenegaux/packages?repo_name=fastDNA" data-view-component="true" class="Link--primary no-underline">
    Packages <span title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>
</a></h2>


      <div class="text-small color-fg-muted">
        No packages published <br>
      </div>



            </div>
          </div>
          <div class="BorderGrid-row" hidden>
            <div class="BorderGrid-cell">
              <include-fragment src="/rmenegaux/fastDNA/used_by_list" accept="text/fragment+html">
</include-fragment>
            </div>
          </div>
          <div class="BorderGrid-row">
            <div class="BorderGrid-cell">
              <h2 class="h4 mb-3">Languages</h2>
<div class="mb-2">
  <span data-view-component="true" class="Progress">
    <span style="background-color:#f34b7d !important;;width: 87.8%;" itemprop="keywords" aria-label="C++ 87.8" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#3572A5 !important;;width: 10.3%;" itemprop="keywords" aria-label="Python 10.3" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#427819 !important;;width: 1.2%;" itemprop="keywords" aria-label="Makefile 1.2" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
    <span style="background-color:#89e051 !important;;width: 0.7%;" itemprop="keywords" aria-label="Shell 0.7" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
</span></div>
<ul class="list-style-none">
    <li class="d-inline">
      <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/rmenegaux/fastDNA/search?l=c%2B%2B"  data-ga-click="Repository, language stats search click, location:repo overview">
        <svg style="color:#f34b7d;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path>
</svg>
        <span class="color-fg-default text-bold mr-1">C++</span>
        <span>87.8%</span>
      </a>
    </li>
    <li class="d-inline">
      <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/rmenegaux/fastDNA/search?l=python"  data-ga-click="Repository, language stats search click, location:repo overview">
        <svg style="color:#3572A5;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path>
</svg>
        <span class="color-fg-default text-bold mr-1">Python</span>
        <span>10.3%</span>
      </a>
    </li>
    <li class="d-inline">
      <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/rmenegaux/fastDNA/search?l=makefile"  data-ga-click="Repository, language stats search click, location:repo overview">
        <svg style="color:#427819;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path>
</svg>
        <span class="color-fg-default text-bold mr-1">Makefile</span>
        <span>1.2%</span>
      </a>
    </li>
    <li class="d-inline">
      <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="/rmenegaux/fastDNA/search?l=shell"  data-ga-click="Repository, language stats search click, location:repo overview">
        <svg style="color:#89e051;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path>
</svg>
        <span class="color-fg-default text-bold mr-1">Shell</span>
        <span>0.7%</span>
      </a>
    </li>
</ul>

            </div>
          </div>
      </div>
</div>
  
</div></div>



  </div>
</div>

    </main>
  </div>

  </div>

          <footer class="footer width-full container-xl p-responsive" role="contentinfo">


  <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6">
    <ul class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mt-2 mt-lg-0 d-flex flex-items-center">
        <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com">
          <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>        <span>
        &copy; 2022 GitHub, Inc.
        </span>
      </li>
    </ul>
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-8 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-terms-of-service" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="3ff63ed66cdc706cdc97e08d1d4be1ae406b6f0194d6c6d3f41a90f914c1f627" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-privacy-statement" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="9465edfc2bbeca0ffc0075fd4f102d9caae45598486c0c5ca32414d37fb685ae" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="8de313c3017dd326c815e6d87aee347caf90aec671676a4cd471d708c26db3a5" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="e3266a1ced766634ce6b9fa9f14e8383bdb8ac1a3c66905f3852bb18970a0e04" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}">Status</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com">Docs</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://support.github.com?tags=dotcom-footer" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="295f02f7b1469d0aaefb275e2628c4f421829d38e719153ee6bdd955301f47cb" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="372eb183062cb6a60c3cbb9507da40bd958f656213561dddd20efd3c8e488cfa" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Pricing&quot;,&quot;label&quot;:&quot;text:Pricing&quot;}">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://docs.github.com" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="b773986125b0d0a86c0bd8ffa29c6ece252be2a6ac634f09cd621685ccf15662" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to api&quot;,&quot;label&quot;:&quot;text:api&quot;}">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://services.github.com" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="e0e42e2145618ac6688b3a12a79a63d4a7c2ffe9f09ce0f17a98b9721ddd8be0" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to training&quot;,&quot;label&quot;:&quot;text:training&quot;}">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-hydro-click="{&quot;event_type&quot;:&quot;analytics.event&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;,&quot;originating_url&quot;:&quot;https://github.com/rmenegaux/fastDNA&quot;,&quot;user_id&quot;:14911686}}" data-hydro-click-hmac="f093c88bb68f063cbac34322ff762dd18e1f3acaa85984c32b068fc698f951a5" data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to blog&quot;,&quot;label&quot;:&quot;text:blog&quot;}">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-fg-muted"></span>
  </div>
</footer>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden>
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
    <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default color-fg-default hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;">
  </div>
</div>

    <template id="snippet-clipboard-copy-button">
  <div class="zeroclipboard-container position-absolute right-0 top-0">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0 tooltipped-no-delay" data-copy-feedback="Copied!" data-tooltip-direction="w">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2">
    <path fill-rule="evenodd" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 010 1.5h-1.5a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-1.5a.75.75 0 011.5 0v1.5A1.75 1.75 0 019.25 16h-7.5A1.75 1.75 0 010 14.25v-7.5z"></path><path fill-rule="evenodd" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0114.25 11h-7.5A1.75 1.75 0 015 9.25v-7.5zm1.75-.25a.25.25 0 00-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 00.25-.25v-7.5a.25.25 0 00-.25-.25h-7.5z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none m-2">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
    </clipboard-copy>
  </div>
</template>


    <style>
      .user-mention[href$="/phenolophthaleinum"] {
        color: var(--color-user-mention-fg);
        background-color: var(--color-user-mention-bg);
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


  </body>
</html>

'''
# print(re.findall(r'.*@.*\.\w+', text))
print(re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text))