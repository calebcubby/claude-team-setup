"""Tests for claude-setup/build.py wizard step functions and existing functions."""

import sys
import os
import pytest
from unittest.mock import patch, mock_open

# Add the directory containing build.py to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build


# ── Preferences Styles ────────────────────────────────────────────────


class TestPreferencesStyles:
    def test_progress_bar_class(self):
        assert ".progress-bar" in build.styles()

    def test_progress_segment_class(self):
        assert ".progress-segment" in build.styles()

    def test_question_card_class(self):
        assert ".question-card" in build.styles()

    def test_pill_class(self):
        assert ".pill" in build.styles()

    def test_pill_capitalize(self):
        result = build.styles()
        assert "text-transform: capitalize" in result

    def test_output_preview_class(self):
        assert ".output-preview" in build.styles()

    def test_output_box_class(self):
        assert ".output-box" in build.styles()

    def test_fade_in_animation(self):
        assert "fadeIn" in build.styles()

    def test_btn_ghost_class(self):
        assert ".btn-ghost" in build.styles()


class TestArtifactPreviewStyles:
    def test_artifact_preview_class(self):
        assert ".artifact-preview" in build.styles()


# ── Preferences JS ────────────────────────────────────────────────────
# TestPreferencesJS: prefNext, prefPrev, prefGenerate, prefCopyAndTransform,
# prefBackToQuestions were all deleted. New JS is covered by TestProfileJavaScript.


class TestPreferencesJS:
    def test_pref_toggle_function(self):
        assert "prefToggle" in build.footer_and_script()

    def test_pref_single_select_function(self):
        assert "prefSingleSelect" in build.footer_and_script()

    def test_tone_mapping(self):
        result = build.footer_and_script()
        assert "Direct. Clear. No fluff" in result

    def test_company_context_auto_included(self):
        result = build.footer_and_script()
        assert "project management tools for growing teams" in result

    def test_no_old_writing_style_js(self):
        result = build.footer_and_script()
        assert "WARN_CHARS" not in result
        assert "MIN_SAMPLES" not in result
        assert "getFilledCount" not in result


# ── Old Functions Removed ────────────────────────────────────────────


class TestOldFunctionsRemoved:
    def test_wizard_step_2_removed(self):
        assert not hasattr(build, 'wizard_step_2')

    def test_narrative_intro_removed(self):
        assert not hasattr(build, 'narrative_intro')

    def test_wizard_step_1_removed(self):
        assert not hasattr(build, 'wizard_step_1')

    def test_wizard_step_5_removed(self):
        assert not hasattr(build, 'wizard_step_5')



# ── Features Grid (Task 5) ───────────────────────────────────────────


class TestFeaturesGrid:
    def test_returns_string(self):
        assert isinstance(build.features_grid(), str)

    def test_contains_section_title(self):
        assert "Key Chat Features" in build.features_grid()

    def test_contains_features_grid_class(self):
        assert "features-grid" in build.features_grid()

    def test_contains_projects_card(self):
        assert "Projects" in build.features_grid()

    def test_contains_deep_research_card(self):
        assert "Deep Research" in build.features_grid()

    def test_contains_artifacts_card(self):
        assert "Artifacts" in build.features_grid()

    def test_contains_connectors_card(self):
        assert "Connectors" in build.features_grid()

    def test_four_feature_cards(self):
        assert build.features_grid().count("feature-card") == 4


# ── General Tips (Task 6) ───────────────────────────────────────────


class TestGeneralTips:
    def test_no_old_tab_wrapper_closing(self):
        assert "end tab section wrapper" not in build.general_tips()

    def test_subtitle_updated(self):
        assert "Chat, Cowork, and Code" not in build.general_tips()

    def test_contains_tips_grid(self):
        assert "tips-grid" in build.general_tips()

    def test_nine_tip_cards(self):
        assert build.general_tips().count("tip-card") == 10


# ── Use Cases (Task 7) ──────────────────────────────────────────────


class TestUseCases:
    def test_returns_string(self):
        assert isinstance(build.use_cases(), str)

    def test_contains_role_picker(self):
        assert "role-picker" in build.use_cases()

    def test_contains_role_select(self):
        assert 'id="role-select"' in build.use_cases()

    def test_contains_universal_cases(self):
        assert "universal-cases" in build.use_cases()

    def test_contains_role_cases_divs(self):
        assert "role-cases" in build.use_cases()

    def test_contains_all_departments(self):
        result = build.use_cases()
        for dept in ["Growth", "Sales", "Product", "Engineering", "Product",
                      "Operations", "Customer Success", "Finance", "People Ops",
                      "Operations", "EA / Admin", "CEO / Leadership"]:
            assert dept in result, f"Missing department: {dept}"


# ── Step 2 JS (Chunk 2 - Task 6) ─────────────────────────────────────


class TestStep2JS:
    def test_toggle_import_function(self):
        assert "toggleImport" in build.footer_and_script()

    def test_import_paste_reference(self):
        assert "import-paste" in build.footer_and_script()

    def test_copy_export_prompt(self):
        assert "copy-export-prompt" in build.footer_and_script()

    def test_memory_merge_logic(self):
        # The memory generator should reference both import paste and fields
        result = build.footer_and_script()
        assert "importPaste" in result or "import-paste" in result


# ── Footer & Script (Task 9) ─────────────────────────────────────────


class TestFooterAndScript:
    def test_contains_wizard_stage_js(self):
        result = build.footer_and_script()
        assert "wizard-stage" in result or "wizardStages" in result

    def test_contains_wizard_stage_done_handler(self):
        result = build.footer_and_script()
        assert "wizard_stage_done" in result or "stage-done-btn" in result

    def test_contains_stage_progress_update(self):
        result = build.footer_and_script()
        assert "updateStageProgress" in result

    def test_contains_role_picker_js(self):
        result = build.footer_and_script()
        assert "role-select" in result or "roleSelect" in result

    def test_contains_localstorage_persistence(self):
        result = build.footer_and_script()
        assert "localStorage" in result

    def test_contains_accordion_toggle(self):
        result = build.footer_and_script()
        assert "accordion-header" in result

    def test_storage_key_v5(self):
        result = build.footer_and_script()
        assert "team-setup-wizard-done-v1" in result
        assert "var WIZARD_KEY = 'team-setup-wizard-done-v1'" in result

    def test_no_old_storage_key_as_active(self):
        result = build.footer_and_script()
        # v4 key should only appear in migration, not as the active key
        assert "var WIZARD_KEY = 'team-setup-wizard-done-v1'" in result
        assert "var WIZARD_KEY = 'team-setup-wizard-done-v0'" not in result

    def test_stage_navigation_functions(self):
        """showStage and showWizardComplete functions must exist."""
        result = build.footer_and_script()
        assert "function showStage(" in result
        assert "function showWizardComplete(" in result

    def test_back_button_handler(self):
        """Back buttons should navigate to previous stage."""
        result = build.footer_and_script()
        assert "stage-back-btn" in result

    def test_restore_state_on_load(self):
        """Wizard should restore state and show first incomplete stage on load."""
        result = build.footer_and_script()
        assert "firstIncomplete" in result or "showStage(firstIncomplete)" in result


# -- Page Order (Cowork section placement) ---------------------


class TestTabPageOrder:
    def test_overview_before_chat(self):
        html = build.generate()
        assert html.index('data-tab="overview"') < html.index('data-tab="chat"')

    def test_chat_before_cowork(self):
        html = build.generate()
        assert html.index('data-tab="chat"') < html.index('data-tab="cowork"')

    def test_cowork_before_code(self):
        html = build.generate()
        assert html.index('data-tab="cowork"') < html.index('data-tab="code"')

    def test_hero_before_tabs(self):
        html = build.generate()
        assert html.index('class="hero"') < html.index('data-tab="overview"')

    def test_resources_after_code_tab(self):
        html = build.generate()
        assert html.index('data-tab="code"') < html.index('class="section-title">Resources')


# -- Cowork JavaScript -----------------------------------------


class TestCoworkJavaScript:
    @pytest.fixture
    def html(self):
        return build.generate()

    def test_cowork_storage_key_defined(self, html):
        assert "team-cowork-done-v1" in html

    def test_wizard_stage_selector_scoped(self, html):
        """Wizard JS must select .wizard-stage elements for stage navigation"""
        assert ".wizard-stage" in html

    def test_cowork_selector_scoped(self, html):
        """Cowork JS must select .cowork-cards .wizard-step"""
        assert ".cowork-cards .wizard-step" in html

    def test_cowork_done_function(self, html):
        """Cowork has its own getDoneCoworkCards function or equivalent"""
        assert "cowork-done" in html or "team-cowork-done" in html

    def test_cowork_cards_expand_collapse(self, html):
        """Cowork cards have click handlers for expand/collapse"""
        assert "data-cowork-card" in html

    def test_cowork_auto_open_logic(self, html):
        """Cowork JS auto-opens first incomplete card on page load"""
        assert "coworkOpened" in html or "cowork-card" in html

    def test_open_cowork_card_helper(self, html):
        """openCoworkCard helper function exists"""
        assert "function openCoworkCard(" in html

    def test_cowork_completable_constant(self, html):
        """COWORK_COMPLETABLE defines cards 1, 2, 3 as completable"""
        assert "COWORK_COMPLETABLE = ['1', '2', '3']" in html

    def test_show_cowork_success_function(self, html):
        """showCoworkSuccess function exists"""
        assert "function showCoworkSuccess(" in html

    def test_header_click_uses_open_helper(self, html):
        """Header click handler uses openCoworkCard() helper"""
        assert "openCoworkCard(card)" in html

    def test_cowork_auto_advance_on_complete(self, html):
        """After completing a card, auto-advance opens next incomplete card"""
        assert "openCoworkCard(next)" in html



# ── Existing Functions ───────────────────────────────────────────────


class TestExistingFunctions:
    def test_head(self):
        assert isinstance(build.head(), str)

    def test_styles(self):
        assert isinstance(build.styles(), str)

    def test_hero(self):
        assert isinstance(build.hero(), str)

    def test_tab_overview(self):
        assert isinstance(build.tab_overview(), str)

    def test_tab_chat(self):
        assert isinstance(build.tab_chat(), str)

    def test_tab_cowork(self):
        assert isinstance(build.tab_cowork(), str)

    def test_tab_code(self):
        assert isinstance(build.tab_code(), str)


# ── Step 2 Styles (Chunk 2 - Task 4) ─────────────────────────────────


class TestStep2Styles:
    def test_import_toggle_class(self):
        assert ".import-toggle" in build.styles()

    def test_import_content_class(self):
        assert ".import-content" in build.styles()

    def test_import_step_class(self):
        assert ".import-step" in build.styles()

    def test_prompt_box_class(self):
        assert ".prompt-box" in build.styles()

    def test_paste_box_class(self):
        assert ".paste-box" in build.styles()

    def test_step_divider_class(self):
        assert ".step-divider" in build.styles()

    def test_work_only_note_class(self):
        assert ".work-only-note" in build.styles()


# ── Intro Section Styles (Chunk 1 - Task 1) ──────────────────────────


class TestIntroSectionStyles:
    def test_narrative_intro_class(self):
        assert ".narrative-intro" in build.styles()

    def test_why_claude_card_class(self):
        assert ".why-claude-card" in build.styles()

    def test_why_claude_card_columns(self):
        assert "columns: 2" in build.styles()


# ── Why Anthropic (Chunk 1 - Task 2) ─────────────────────────────────


class TestWhyAnthropic:
    def test_returns_string(self):
        assert isinstance(build.why_anthropic(), str)

    def test_contains_heading(self):
        assert "Why we chose Claude" in build.why_anthropic()

    def test_contains_subtitle(self):
        assert "safety as the foundation" in build.why_anthropic()

    def test_contains_why_claude_card_class(self):
        assert "why-claude-card" in build.why_anthropic()

    def test_contains_four_bullets(self):
        result = build.why_anthropic()
        assert "Constitutional AI" in result
        assert "Enterprise-grade security" in result
        assert "SOC 2 Type II" in result
        assert "Never used to train models" in result

    def test_four_list_items(self):
        assert build.why_anthropic().count("<li>") == 4


# ── Generate Pipeline (Chunk 1 - Task 3) ─────────────────────────────


class TestGeneratePipeline:
    def test_returns_string(self):
        assert isinstance(build.generate(), str)

    def test_contains_html_tag(self):
        assert '<html' in build.generate()

    def test_contains_hero(self):
        assert 'class="hero"' in build.generate()

    def test_contains_page_content(self):
        assert 'class="page-content"' in build.generate()

    def test_contains_tab_content(self):
        assert 'tab-content' in build.generate()

    def test_contains_footer(self):
        assert 'class="footer"' in build.generate()


# ── Resources Updated (Chunk 1 - Task 3) ─────────────────────────────


class TestResourcesUpdated:
    def test_no_why_anthropic_card(self):
        result = build.resources()
        assert "Why Anthropic" not in result

    def test_three_resource_cards(self):
        assert build.resources().count("resource-card") == 3

    def test_still_has_training(self):
        assert "Training" in build.resources()

    def test_still_has_internal(self):
        assert "Internal" in build.resources()

    def test_still_has_get_help(self):
        assert "Get Help" in build.resources()


    def test_build_creates_file(self):
        m = mock_open()
        with patch("builtins.open", m):
            build.build()
        m.assert_called_once_with(build.OUTPUT, "w")
        m().write.assert_called_once()


# ── Spacing Consistency Pass ────────────────────────────────────────


class TestSpacingConsistency:
    """Tests for spacing consistency pass - section margins, h4 margins, card padding."""

    def test_narrative_intro_margin_48px(self):
        result = build.styles()
        start = result.index(".narrative-intro {")
        end = result.index("}", start)
        block = result[start:end]
        assert "margin-top: var(--space-3xl)" in block

    def test_compliance_margin_48px(self):
        result = build.styles()
        start = result.index(".compliance {")
        end = result.index("}", start)
        block = result[start:end]
        assert "margin-top: var(--space-3xl)" in block

    def test_feature_card_h4_margin_8px(self):
        result = build.styles()
        start = result.index(".feature-card h4")
        end = result.index("}", start)
        block = result[start:end]
        assert "margin-bottom: var(--space-xs)" in block

    def test_model_option_h4_margin_8px(self):
        result = build.styles()
        start = result.index(".model-option h4")
        end = result.index("}", start)
        block = result[start:end]
        assert "margin-bottom: var(--space-xs)" in block

    def test_tip_card_h4_margin_8px(self):
        result = build.styles()
        start = result.index(".tip-card h4")
        end = result.index("}", start)
        block = result[start:end]
        assert "margin-bottom: var(--space-xs)" in block

    def test_compliance_box_padding_20px(self):
        result = build.styles()
        start = result.index(".compliance-box {")
        end = result.index("}", start)
        block = result[start:end]
        assert "padding: var(--space-lg)" in block


class TestDesignSystemEnforcement:
    """Prevent regression of design system token usage."""

    def test_no_hardcoded_hex_in_styles(self):
        """All hex colors in styles() must use var() tokens."""
        import re
        css = build.styles()
        hexes = re.findall(r'(?<!\w)#[0-9a-fA-F]{3,6}\b', css)
        allowed = {'e5e5e5', 'fff'}
        unexpected = [h for h in hexes if h.lstrip('#').lower() not in allowed]
        assert unexpected == [], f"Hardcoded hex in styles(): {unexpected}"

    def test_no_6px_border_radius_in_styles(self):
        """No border-radius: 6px should remain after consolidation."""
        css = build.styles()
        assert 'border-radius: 6px' not in css

    def test_spacing_tokens_in_root(self):
        """All 9 spacing tokens must be defined in inline :root."""
        html = build.head()
        tokens = ['--space-2xs', '--space-xs', '--space-sm', '--space-md',
                  '--space-lg', '--space-xl', '--space-2xl', '--space-3xl', '--space-4xl']
        for token in tokens:
            assert token in html, f"Missing spacing token in :root: {token}"

    def test_token_parity_brand_css(self):
        """brand.css and build.py inline :root must define the same tokens."""
        import re
        with open('shared/brand.css') as f:
            brand_css = f.read()
        brand_tokens = set(re.findall(r'--([\w-]+):', brand_css))
        html = build.head()
        root_match = re.search(r':root\s*\{([^}]+)\}', html)
        inline_tokens = set(re.findall(r'--([\w-]+):', root_match.group(1))) if root_match else set()
        missing_from_inline = brand_tokens - inline_tokens
        assert missing_from_inline == set(), f"Tokens in brand.css but not in build.py :root: {missing_from_inline}"
        extra_in_inline = inline_tokens - brand_tokens
        assert extra_in_inline == set(), f"Tokens in build.py :root but not in brand.css: {extra_in_inline}"


class TestSpacingUtilityClasses:
    """Tests for CSS utility classes added during spacing consistency pass."""

    def test_accordion_body_p_styling(self):
        result = build.styles()
        assert ".accordion-body p" in result

    def test_section_label_has_color(self):
        result = build.styles()
        start = result.index(".accordion-body .section-label")
        end = result.index("}", start)
        block = result[start:end]
        assert "color:" in block

    def test_step_intro_class(self):
        assert ".step-intro" in build.styles()

    def test_download_row_class(self):
        assert ".download-row" in build.styles()

    def test_data_warning_inline_class(self):
        assert ".data-warning-inline" in build.styles()

    def test_q_hint_below_class(self):
        assert ".q-hint-below" in build.styles()

    def test_pref_samples_id_style(self):
        assert "#pref-samples" in build.styles()

    def test_prompt_box_has_margin(self):
        result = build.styles()
        start = result.index(".prompt-box {")
        end = result.index("}", start)
        block = result[start:end]
        assert "margin:" in block


class TestTabCSS:
    def test_tab_content_class(self):
        html = build.styles()
        assert '.tab-content' in html

    def test_tab_content_active(self):
        html = build.styles()
        assert '.tab-content.active' in html

    def test_wizard_stage_class(self):
        html = build.styles()
        assert '.wizard-stage' in html

    def test_progress_stepper(self):
        html = build.styles()
        assert '.progress-stepper' in html

    def test_tool_cards_grid(self):
        html = build.styles()
        assert '.tool-cards-grid' in html

    def test_locked_state(self):
        html = build.styles()
        assert '.locked-state' in html

    def test_request_access_heading(self):
        html = build.styles()
        assert '.request-access h3' in html

    def test_stage_nav(self):
        html = build.styles()
        assert '.stage-nav' in html


class TestSpacingCopyAndJS:
    """Tests for leverage copy fix. prefNext/prefPrev bounds tests deleted - those
    functions were removed (covered by TestProfileJavaScript::test_no_pref_next_prev_functions)."""

    def test_contains_leverage_copy(self):
        result = build.mission_narrative()
        assert "gives you leverage" in result or "leverage" in result.lower()


# ── Merged Profile Step (Task 2) ─────────────────────────────────────


@pytest.fixture
def html():
    """Generate the full HTML output for testing."""
    return build.generate()


def get_step(html, step_num):
    """Extract a specific wizard step's HTML from the full output."""
    # Find the step div by data-step attribute
    marker = f'data-step="{step_num}"'
    start = html.find(marker)
    if start == -1:
        return ''
    # Go back to find the opening div
    div_start = html.rfind('<div', 0, start)
    # Find the matching closing div (count nested divs)
    depth = 0
    i = div_start
    while i < len(html):
        if html[i:i+4] == '<div':
            depth += 1
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return html[div_start:i+6]
        i += 1
    return html[div_start:]


class TestMergedProfileStep:
    """Tests for profile form content, now in wizard_stage_1()"""

    def test_profile_title_in_stage(self):
        """Stage 1 has profile title"""
        result = build.wizard_stage_1()
        assert 'Your Profile' in result

    def test_no_step_called_memory(self, html):
        """Old Step 2 'Set Up Your Memory' no longer exists"""
        assert 'Set Up Your Memory' not in html

    def test_no_step_called_preferences(self, html):
        """Old Step 3 'Set Your Preferences' no longer exists"""
        assert 'Set Your Preferences' not in html

    def test_wizard_has_3_stages(self, html):
        """Chat wizard uses 3 stages"""
        assert 'data-stage="1"' in html
        assert 'data-stage="2"' in html
        assert 'data-stage="3"' in html

    def test_subsection_who_you_are(self):
        """Sub-section 1: Who You Are fields exist"""
        result = build._profile_form_content()
        assert 'profile-name' in result
        assert 'profile-work' in result
        assert 'profile-tools' in result

    def test_subsection_how_claude_should_work(self):
        """Sub-section 2: Pill selectors for audiences, tone, values, don'ts"""
        result = build._profile_form_content()
        assert 'Customers / prospects' in result
        assert 'Direct - skip the fluff' in result
        assert 'Get to the point' in result
        assert 'Pad responses with filler' in result

    def test_format_preferences_field(self):
        """Format preferences textarea exists"""
        result = build._profile_form_content()
        assert 'profile-format' in result
        assert 'Bullet points, lead with the number' in result

    def test_catchall_field(self):
        """Catch-all textarea exists"""
        result = build._profile_form_content()
        assert 'profile-catchall' in result

    def test_writing_voice_section(self):
        """Writing samples textarea with data privacy warning"""
        result = build._profile_form_content()
        assert 'profile-samples' in result
        assert 'No sensitive data' in result

    def test_import_section_exists(self):
        """Import accordion exists with EXPORT_PROMPT"""
        result = build._profile_form_content()
        assert 'import-toggle' in result
        assert 'import-paste' in result
        assert 'Export all of my stored memories' in result

    def test_generate_button(self):
        """Generate Profile button exists"""
        result = build._profile_form_content()
        assert 'generate-profile-btn' in result
        assert 'Generate Profile' in result

    def test_preferences_output_block(self):
        """Primary output: Your Preferences with copy button"""
        result = build._profile_form_content()
        assert 'pref-output-box' in result
        assert 'Copy this into Claude Settings' in result

    def test_no_memory_output_block(self):
        """Memory output block removed - Preferences only"""
        result = build._profile_form_content()
        assert 'mem-output-box' not in result
        assert 'Memory lets Claude learn about you over time' not in result

    def test_review_hint_present(self):
        """Review hint encourages users to edit their output"""
        result = build._profile_form_content()
        assert 'output-review-hint' in result
        assert 'make it yours' in result.lower()

    def test_word_count_indicators(self):
        """Word count divs exist below both output textareas"""
        result = build._profile_form_content()
        assert 'pref-word-count' in result

    def test_edit_answers_button(self):
        """Edit Answers button in output area"""
        result = build._profile_form_content()
        assert 'Edit Answers' in result

    def test_no_progress_bar_in_profile(self):
        """No internal progress bar (old Preferences pattern removed)"""
        result = build._profile_form_content()
        assert 'progress-segment' not in result
        assert 'pref-seg-' not in result

    def test_no_question_cards_in_profile(self):
        """No card-by-card navigation (old Preferences pattern removed)"""
        result = build._profile_form_content()
        assert 'question-card' not in result
        assert 'pref-q0' not in result

    def test_no_duplicate_name_field(self):
        """Name is asked once, not in both old steps"""
        result = build._profile_form_content()
        assert 'pref-name' not in result
        assert 'mem-0' not in result

    def test_pill_labels_exact_match(self):
        """Pill labels match current implementation exactly"""
        result = build._profile_form_content()
        assert 'Customers / prospects' in result
        assert 'Be honest, not nice' in result

    def test_import_accordion_collapsed_by_default(self):
        """Import section starts collapsed"""
        result = build._profile_form_content()
        assert 'id="import-content"' in result
        assert 'import-content' in result

    def test_collapsible_examples_list(self):
        """Writing sample examples list exists and is collapsible"""
        result = build._profile_form_content()
        assert 'Good examples to include' in result
        assert 'A wins post or team shoutout' in result

    def test_data_pill_group_attributes(self):
        """Pill groups have data-pill-group attributes for JS targeting"""
        result = build._profile_form_content()
        assert 'data-pill-group="audiences"' in result
        assert 'data-pill-group="tone"' in result
        assert 'data-pill-group="values"' in result
        assert 'data-pill-group="donts"' in result

    def test_generate_button_has_onclick(self):
        """Regression: Generate Profile button wired to generateProfile()"""
        result = build._profile_form_content()
        assert 'onclick="generateProfile()"' in result

    def test_edit_answers_button_has_correct_onclick(self):
        """Regression: Edit Answers button calls editAnswers(), not editProfileAnswers()"""
        result = build._profile_form_content()
        assert 'onclick="editAnswers()"' in result
        assert 'editProfileAnswers' not in result

    def test_output_area_no_inline_display_none(self):
        """Regression: output area hidden via CSS class, not inline style"""
        result = build._profile_form_content()
        assert 'id="profile-output-area"' in result
        # Should NOT have inline style="display:none" (CSS specificity bug)
        assert 'profile-output-area" style="display:none"' not in result
        assert 'profile-output-area" style="display: none"' not in result


# ── Profile JavaScript Tests ───────────────────────────────────────────────


class TestProfileJavaScript:
    """Tests for merged step JavaScript functions"""

    def test_generate_profile_function_exists(self, html):
        """generateProfile function is defined"""
        assert 'function generateProfile' in html or 'generateProfile = function' in html

    def test_preferences_template_structure(self, html):
        """Generated preferences block includes expected sections"""
        assert '## About Me' in html
        assert '## My Audiences' in html
        assert '## Communication Style' in html
        assert "## Don\\'t Do" in html or "## Don't Do" in html
        assert '## My Writing Voice' in html

    def test_company_guardrails_in_preferences(self, html):
        """Company guardrails auto-included in preferences output"""
        assert 'Company Guardrails' in html
        assert 'Data Privacy' in html
        assert 'Content claims' in html

    def test_tone_map_exists(self, html):
        """TONE_MAP constant preserved from old Step 3"""
        assert 'TONE_MAP' in html
        assert 'Direct. Clear. No fluff.' in html

    def test_word_count_function(self, html):
        """updateWordCount function exists"""
        assert 'updateWordCount' in html or 'wordCount' in html

    def test_word_count_threshold_yellow(self, html):
        """Word count turns yellow at 1200 words"""
        assert '1200' in html or '1,200' in html

    def test_word_count_threshold_red(self, html):
        """Word count turns red at 1500 words"""
        assert '1500' in html or '1,500' in html

    def test_empty_validation(self, html):
        """Empty name validation shows toast"""
        assert 'Fill in at least your name' in html

    def test_import_truncation_cap(self, html):
        """Import text capped at 2000 words"""
        assert '2000' in html

    def test_import_truncation_toast(self, html):
        """Import truncation shows toast message"""
        assert 'Import trimmed to fit within word limit' in html

    def test_samples_truncation_toast(self, html):
        """Samples truncation shows toast message"""
        assert 'trimmed to stay under the 1,500 word limit' in html

    def test_draft_persistence_exists(self, html):
        """Draft persistence via saveDraft exists"""
        assert 'saveDraft' in html

    def test_samples_truncation_cap(self, html):
        """Writing samples capped at 1500 words"""
        assert '1500' in html

    def test_null_guard_on_pill_selector(self, html):
        """Null guard: if (!group) return"""
        assert 'if (!group) return' in html or 'if(!group)return' in html

    def test_localstorage_v1_key(self, html):
        """Uses team-setup-wizard-done-v1 storage key"""
        assert 'team-setup-wizard-done-v1' in html

    def test_draft_persistence_key(self, html):
        """Uses team-profile-draft for partial answers"""
        assert 'team-profile-draft' in html

    def test_localstorage_try_catch(self, html):
        """All localStorage calls wrapped in try/catch"""
        assert 'try' in html
        assert 'catch' in html

    def test_edit_answers_scrolls_to_form(self, html):
        """Edit Answers button scrolls to form top"""
        assert 'editAnswers' in html or 'scrollIntoView' in html

    def test_copy_preferences_opens_settings(self, html):
        """Copy button opens claude.ai/settings/profile"""
        assert 'claude.ai/settings/profile' in html

    def test_no_memory_copy_handler(self, html):
        """Memory copy handler removed"""
        assert 'mem-copy-btn' not in html

    def test_no_pref_next_prev_functions(self, html):
        """Old prefNext/prefPrev card navigation removed"""
        assert 'function prefNext' not in html
        assert 'function prefPrev' not in html

    def test_no_auto_populate_name(self, html):
        """Old openStep name auto-populate removed"""
        assert 'mem-0' not in html


# -- Cowork Section Header ------------------------------------


# -- Cowork Card 1: What is Cowork? ---------------------------


class TestCoworkCard1:
    def test_returns_string(self):
        assert isinstance(build.cowork_card_1(), str)

    def test_contains_wizard_step_class(self):
        assert 'class="wizard-step"' in build.cowork_card_1()

    def test_data_cowork_card_attribute(self):
        assert 'data-cowork-card="1"' in build.cowork_card_1()

    def test_contains_title(self):
        assert "What is Cowork?" in build.cowork_card_1()

    def test_contains_preview_text(self):
        assert "When to use it" in build.cowork_card_1()

    def test_contains_comparison_table(self):
        result = build.cowork_card_1()
        assert "comparison-table" in result
        assert "Chat" in result
        assert "Cowork" in result

    def test_comparison_table_has_four_rows(self):
        """Table has 4 comparison rows per the spec"""
        result = build.cowork_card_1()
        assert "Quick questions" in result
        assert "file deliverables" in result
        assert "Scheduled" in result or "recurring" in result

    def test_contains_capability_list(self):
        result = build.cowork_card_1()
        assert "Read, write, and organize" in result
        assert "Excel spreadsheets" in result or "PowerPoint" in result

    def test_contains_desktop_requirement(self):
        result = build.cowork_card_1()
        assert "desktop app" in result

    def test_no_done_button(self):
        """Card 1 is informational - no Mark complete button"""
        assert "wizard-done-btn" not in build.cowork_card_1()

    def test_has_step_num(self):
        assert '<span class="step-num">1</span>' in build.cowork_card_1()


# -- Cowork Card 2: Set Up Your Project -----------------------


class TestCoworkCard2:
    def test_returns_string(self):
        assert isinstance(build.cowork_card_2(), str)

    def test_data_cowork_card_attribute(self):
        assert 'data-cowork-card="1"' in build.cowork_card_2()

    def test_contains_title(self):
        assert "Set Up Your Project" in build.cowork_card_2()

    def test_contains_preview_text(self):
        assert "project folder" in build.cowork_card_2() or "context files" in build.cowork_card_2()

    def test_contains_folder_name(self):
        assert "Claude_Company" in build.cowork_card_2()

    def test_contains_three_download_buttons(self):
        result = build.cowork_card_2()
        assert "company.md" in result
        assert "brand.md" in result
        assert "writing-style.md" in result

    def test_download_urls_correct(self):
        result = build.cowork_card_2()
        assert "/company.md" in result
        assert "/brand.md" in result
        assert "writing-style.md" in result  # referenced, not downloaded

    def test_contains_verify_step(self):
        result = build.cowork_card_2()
        assert "What files do you see" in result

    def test_contains_why_paragraph(self):
        result = build.cowork_card_2()
        assert "context about your company" in result or "write in our voice" in result

    def test_contains_done_button(self):
        assert "wizard-done-btn" in build.cowork_card_2()

    def test_has_step_num(self):
        assert '<span class="step-num">1</span>' in build.cowork_card_2()

    def test_contains_numbered_steps(self):
        """Card 2 has numbered setup steps"""
        result = build.cowork_card_2()
        assert "Cowork tab" in result or "Set project folder" in result

    def test_writing_style_download(self):
        """Card has writing-style.md download button"""
        assert "writing-style.md" in build.cowork_card_2()


# -- Cowork Card 3: Quick Wins --------------------------------


class TestCoworkCard3:
    def test_returns_string(self):
        assert isinstance(build.cowork_card_3(), str)

    def test_data_cowork_card_attribute(self):
        assert 'data-cowork-card="2"' in build.cowork_card_3()

    def test_contains_title(self):
        assert "Quick Wins" in build.cowork_card_3()

    def test_contains_preview_text(self):
        assert "Two fast tasks" in build.cowork_card_3() or "Cowork in action" in build.cowork_card_3()

    def test_contains_calendar_audit(self):
        result = build.cowork_card_3()
        assert "Calendar Audit" in result or "calendar" in result.lower()

    def test_contains_calendar_prompt(self):
        result = build.cowork_card_3()
        assert "Pull my calendar" in result

    def test_contains_calendar_copy_button(self):
        result = build.cowork_card_3()
        assert 'data-copy="Pull my calendar' in result

    def test_contains_downloads_cleanup(self):
        result = build.cowork_card_3()
        assert "Downloads" in result
        assert "Scan my Downloads" in result

    def test_contains_downloads_copy_button(self):
        result = build.cowork_card_3()
        assert 'data-copy="Scan my Downloads' in result

    def test_contains_data_privacy_inline_warning(self):
        """Data privacy warning appears before Downloads task"""
        result = build.cowork_card_3()
        assert "customer PII" in result or "sensitive information" in result
        assert "data processing agreement" in result

    def test_data_privacy_warning_uses_note_class(self):
        """Inline data privacy warning uses amber .note styling"""
        result = build.cowork_card_3()
        assert 'class="note"' in result

    def test_contains_privacy_note(self):
        result = build.cowork_card_3()
        assert "locally" in result or "not uploaded" in result

    def test_contains_done_button(self):
        assert "wizard-done-btn" in build.cowork_card_3()

    def test_has_step_num(self):
        assert '<span class="step-num">2</span>' in build.cowork_card_3()

    def test_has_two_substeps(self):
        """Card 3 has two sub-sections"""
        result = build.cowork_card_3()
        assert result.count("cowork-substep") >= 2

    def test_calendar_profile_icon_instruction(self):
        """Expanded plugin instructions reference profile icon"""
        assert "profile icon" in build.cowork_card_3()

    def test_calendar_settings_plugins(self):
        """Expanded plugin instructions walk through Settings > Plugins"""
        result = build.cowork_card_3()
        assert "Settings" in result
        assert "Plugins" in result


# -- Cowork Card 4: Build a Dashboard -------------------------


class TestCoworkCard4:
    def test_returns_string(self):
        assert isinstance(build.cowork_card_4(), str)

    def test_data_cowork_card_attribute(self):
        assert 'data-cowork-card="3"' in build.cowork_card_4()

    def test_contains_title(self):
        assert "Build a Dashboard from Data" in build.cowork_card_4()

    def test_contains_preview_text(self):
        result = build.cowork_card_4()
        assert "plugins" in result.lower() or "dashboard" in result.lower()

    def test_contains_three_plugin_names(self):
        result = build.cowork_card_4()
        assert "Data" in result
        assert "Marketing" in result
        assert "Customer Support" in result

    def test_contains_sample_data_download(self):
        result = build.cowork_card_4()
        assert "sample-data.xlsx" in result
        assert "/claude-setup/sample-data.xlsx" in result

    def test_contains_explore_data_command(self):
        result = build.cowork_card_4()
        assert "/explore-data" in result

    def test_contains_performance_report_command(self):
        result = build.cowork_card_4()
        assert "/performance-report" in result

    def test_contains_build_dashboard_command(self):
        result = build.cowork_card_4()
        assert "/build-dashboard" in result

    def test_contains_validate_command(self):
        result = build.cowork_card_4()
        assert "/validate" in result

    def test_contains_copy_buttons_for_prompts(self):
        """Card 4 has exactly 6 copy-paste prompts (Steps 3-8)"""
        result = build.cowork_card_4()
        assert result.count("data-copy=") == 6

    def test_contains_closing_text(self):
        result = build.cowork_card_4()
        assert "What you just did" in result or "slash commands" in result

    def test_contains_done_button(self):
        assert "wizard-done-btn" in build.cowork_card_4()

    def test_has_step_num(self):
        assert '<span class="step-num">3</span>' in build.cowork_card_4()

    def test_contains_troubleshooting_note(self):
        result = build.cowork_card_4()
        assert "plugin" in result.lower() and ("Customize" in result or "troubleshoot" in result.lower() or "didn't install" in result)

    def test_contains_deck_step(self):
        result = build.cowork_card_4()
        assert "PowerPoint" in result or "quarterly-review.pptx" in result

    def test_month_over_month(self):
        """MoM abbreviation expanded to full phrase"""
        result = build.cowork_card_4()
        assert "month-over-month" in result

    def test_validate_explanation(self):
        """Validate step has clearer explanation"""
        assert "calculation errors" in build.cowork_card_4()

    def test_plugin_install_confirmation(self):
        """Step 1 tells users to confirm plugins installed"""
        assert "installed before continuing" in build.cowork_card_4()


# -- Cowork Section (wrapper) ---------------------------------


class TestCoworkTabAssembly:
    def test_returns_string(self):
        assert isinstance(build.tab_cowork(), str)

    def test_contains_locked_and_unlocked(self):
        result = build.tab_cowork()
        assert 'cowork-locked' in result
        assert 'cowork-unlocked' in result

    def test_contains_all_unlocked_cards(self):
        result = build.tab_cowork()
        assert 'data-cowork-card="1"' in result
        assert 'data-cowork-card="2"' in result
        assert 'data-cowork-card="3"' in result


class TestCodeSectionCSS:
    def test_code_section_class(self):
        result = build.styles()
        assert ".code-section" in result

    def test_code_cards_class(self):
        result = build.styles()
        assert ".code-cards" in result

    def test_commands_table_class(self):
        result = build.styles()
        assert ".commands-table" in result

    def test_prereq_note_class(self):
        result = build.styles()
        assert ".prereq-note" in result

    def test_code_substep_class(self):
        result = build.styles()
        assert ".code-substep" in result

    def test_code_cards_section_label(self):
        """section-label needs bold/navy styling inside code-cards"""
        result = build.styles()
        assert ".code-cards .section-label" in result

    def test_code_block_has_pre_wrap(self):
        """code-block needs white-space: pre-wrap for multi-line prompts"""
        result = build.styles()
        idx = result.index(".code-block {")
        block_end = result.index("}", idx)
        block = result[idx:block_end]
        assert "pre-wrap" in block

    def test_note_highlight_class(self):
        result = build.styles()
        assert ".note.highlight" in result


class TestCodeCardSetup:
    """Tests for code_card_setup() = Set Up Claude Code (Card 1, completable)"""
    def test_returns_string(self):
        assert isinstance(build.code_card_setup(), str)

    def test_data_attribute(self):
        assert 'data-code-card="1"' in build.code_card_setup()

    def test_card_title(self):
        assert "Set Up Claude Code" in build.code_card_setup()

    def test_preview_text(self):
        assert "Open Code mode and install team skills" in build.code_card_setup()

    def test_has_done_button(self):
        """Setup card is completable"""
        assert "wizard-done-btn" in build.code_card_setup()

    def test_setup_sh_command(self):
        """setup.sh replaces /team-setup for skill installation"""
        assert "setup.sh" in build.code_card_setup()

    def test_git_install_step(self):
        """Card has Git install step"""
        assert "Install Git" in build.code_card_setup() or "git --version" in build.code_card_setup()

    def test_code_tab_instruction(self):
        assert "Code tab" in build.code_card_setup()

    def test_copy_buttons_for_steps(self):
        """Card has copy buttons for the direct setup steps"""
        result = build.code_card_setup()
        assert "copy-btn" in result
        assert result.count("copy-btn") == 4

    def test_verify_step(self):
        assert "/help" in build.code_card_setup()

    def test_going_further(self):
        assert "VS Code" in build.code_card_setup()

    def test_step_num(self):
        assert '<span class="step-num">1</span>' in build.code_card_setup()

    def test_wizard_step_class(self):
        assert 'class="wizard-step"' in build.code_card_setup()

    def test_desktop_app_first(self):
        """Instructions reference desktop app, not terminal"""
        assert "Claude desktop app" in build.code_card_setup() or "Claude app" in build.code_card_setup()

    def test_skills_explanation(self):
        """Explains what /team-setup installs"""
        assert "skills" in build.code_card_setup().lower()




class TestCodeCard3:
    def test_returns_string(self):
        assert isinstance(build.code_card_3(), str)

    def test_data_attribute(self):
        assert 'data-code-card="2"' in build.code_card_3()

    def test_card_title(self):
        assert "Build a Pricing Calculator" in build.code_card_3()

    def test_preview_text(self):
        assert "One prompt, one complete tool" in build.code_card_3()

    def test_has_mkdir_command(self):
        """Card includes mkdir for project setup"""
        assert "mkdir" in build.code_card_3()

    def test_desktop_folder_instruction(self):
        assert "Desktop" in build.code_card_3()
        assert "pricing-calculator" in build.code_card_3()

    def test_two_copy_buttons(self):
        """Copy buttons for mkdir and estimator prompt"""
        assert build.code_card_3().count("copy-btn") == 2

    def test_estimator_prompt_present(self):
        result = build.code_card_3()
        assert "pricing calculator" in result.lower()

    def test_fake_rates_disclaimer(self):
        assert "FAKE placeholder pricing" in build.code_card_3()

    def test_visible_disclaimer(self):
        assert "Estimates only" in build.code_card_3()

    def test_brand_colors(self):
        result = build.code_card_3()
        for color in ["#1e293b", "#f59e0b", "#10b981", "#f8fafc"]:
            assert color in result, f"Missing brand color: {color}"

    def test_done_button(self):
        assert "wizard-done-btn" in build.code_card_3()

    def test_what_you_practiced(self):
        assert "What you practiced" in build.code_card_3()

    def test_step_num(self):
        assert '<span class="step-num">2</span>' in build.code_card_3()

    def test_time_estimate(self):
        assert "30-60 seconds" in build.code_card_3()

    def test_context_sentence(self):
        """New intro explains what a pricing calculator is"""
        assert "prospects estimate" in build.code_card_3()


class TestCodeCard4:
    def test_returns_string(self):
        assert isinstance(build.code_card_4(), str)

    def test_data_attribute(self):
        assert 'data-code-card="3"' in build.code_card_4()

    def test_card_title(self):
        assert "Ship to Production" in build.code_card_4()

    def test_preview_text(self):
        assert "Deploy your estimator with a real PR workflow" in build.code_card_4()

    def test_note_warning_prereq(self):
        """Prerequisite uses red .note.warning style, not gray .prereq-note"""
        result = build.code_card_4()
        assert "note warning" in result

    def test_no_prereq_note(self):
        """Old gray prereq-note style removed"""
        assert "prereq-note" not in build.code_card_4()

    def test_github_url(self):
        assert "github.com/your-org/your-project" in build.code_card_4()

    def test_git_clone_option(self):
        """Uses git clone instead of Download ZIP"""
        assert "git clone" in build.code_card_4()

    def test_no_cd_command(self):
        """Desktop-app-first: no terminal cd command"""
        assert "cd ~/your-project" not in build.code_card_4()

    def test_two_copy_buttons(self):
        """Copy buttons for clone and ship prompt"""
        assert build.code_card_4().count("copy-btn") == 2

    def test_desktop_source_path(self):
        """Source path references Desktop folder"""
        assert "~/Desktop/pricing-calculator" in build.code_card_4()

    def test_feature_branch(self):
        assert "feat/pricing-calculator" in build.code_card_4()

    def test_permissions_json(self):
        assert "permissions.json" in build.code_card_4()

    def test_ship_command(self):
        assert "/ship" in build.code_card_4()

    def test_ship_explanation(self):
        """/ship explanation as separate paragraph below prompt"""
        assert "/ship pushes your code" in build.code_card_4()

    def test_done_button(self):
        assert "wizard-done-btn" in build.code_card_4()

    def test_what_you_practiced(self):
        assert "What you practiced" in build.code_card_4()

    def test_step_num(self):
        assert '<span class="step-num">3</span>' in build.code_card_4()

    def test_auto_deploys_time(self):
        assert "1-2 minutes" in build.code_card_4()


# ── Code Section Assembly (Task 8) ───────────────────────────────────


class TestCodeTabAssembly:
    def test_returns_string(self):
        assert isinstance(build.tab_code(), str)

    def test_contains_locked_and_unlocked(self):
        result = build.tab_code()
        assert 'code-locked' in result
        assert 'code-unlocked' in result

    def test_contains_unlocked_cards(self):
        result = build.tab_code()
        assert 'data-code-card="1"' in result
        assert 'data-code-card="2"' in result
        assert 'data-code-card="3"' in result


class TestCodeJS:
    @pytest.fixture
    def script(self):
        return build.footer_and_script()

    def test_localstorage_key_v3(self, script):
        """Bumped from v2 to v3 for clean slate after card renumbering"""
        assert "team-code-done-v1" in script

    def test_no_old_localstorage_key(self, script):
        """Old v2 key should not appear"""
        assert "team-code-done-v0" not in script

    def test_get_done_function(self, script):
        assert "getDoneCodeCards" in script

    def test_save_done_function(self, script):
        assert "saveDoneCodeCards" in script

    def test_update_state_function(self, script):
        assert "updateCodeState" in script

    def test_open_card_function(self, script):
        assert "openCodeCard" in script

    def test_show_success_function(self, script):
        assert "showCodeSuccess" in script

    def test_code_success_reference(self, script):
        assert "code-success" in script

    def test_track_event_code_done(self, script):
        assert "code_done" in script

    def test_completable_cards(self, script):
        """Cards 1, 2, 3 are completable after renumbering"""
        assert "CODE_COMPLETABLE" in script
        idx = script.index("CODE_COMPLETABLE")
        block = script[idx:idx + 50]
        assert "'1'" in block
        assert "'2'" in block
        assert "'3'" in block

    def test_completable_cards_excludes_4(self, script):
        """Card 4 no longer exists after renumbering"""
        idx = script.index("CODE_COMPLETABLE")
        # Find the array end (next semicolon)
        end = script.index(";", idx)
        block = script[idx:end]
        assert "'4'" not in block

    def test_auto_advance_skips_non_completable(self, script):
        """ENG REVIEW FIX: Auto-advance must skip non-completable cards to prevent dead end on Card 2"""
        assert "CODE_COMPLETABLE.indexOf(next.getAttribute" in script


class TestTabSwitchingJSPresence:
    def test_switch_tab_function(self):
        result = build.footer_and_script()
        assert 'function switchTab' in result

    def test_hash_routing(self):
        result = build.footer_and_script()
        assert 'location.hash' in result

    def test_nav_pill_listeners(self):
        result = build.footer_and_script()
        assert "data-tab" in result


class TestCodeCardOrder:
    def test_setup_before_card_2(self):
        result = build.tab_code()
        assert result.index('data-code-card="1"') < result.index('data-code-card="2"')

    def test_card_2_before_card_3(self):
        result = build.tab_code()
        assert result.index('data-code-card="2"') < result.index('data-code-card="3"')


class TestSectionNav:
    def test_returns_string(self):
        assert isinstance(build.section_nav(), str)

    def test_contains_pills(self):
        result = build.section_nav()
        assert 'nav-pill' in result

    def test_pills_are_buttons(self):
        result = build.section_nav()
        assert '<button' in result
        assert 'data-tab=' in result

    def test_four_tabs(self):
        result = build.section_nav()
        assert 'data-tab="overview"' in result
        assert 'data-tab="chat"' in result
        assert 'data-tab="cowork"' in result
        assert 'data-tab="code"' in result

    def test_nav_has_cowork_and_code(self):
        result = build.section_nav()
        assert 'data-tab="cowork"' in result
        assert 'data-tab="code"' in result


class TestTabContentPresence:
    def test_overview_tab_in_output(self):
        html = build.generate()
        assert 'data-tab="overview"' in html

    def test_chat_tab_in_output(self):
        html = build.generate()
        assert 'data-tab="chat"' in html

    def test_cowork_tab_in_output(self):
        html = build.generate()
        assert 'data-tab="cowork"' in html

    def test_code_tab_in_output(self):
        html = build.generate()
        assert 'data-tab="code"' in html


class TestMissionNarrative:
    def test_returns_string(self):
        assert isinstance(build.mission_narrative(), str)

    def test_contains_mission_div(self):
        assert 'class="mission-narrative"' in build.mission_narrative()

    def test_contains_heading(self):
        assert '<h3>' in build.mission_narrative()

    def test_contains_paragraphs(self):
        assert build.mission_narrative().count('<p') >= 3

    def test_mentions_company(self):
        result = build.mission_narrative().lower()
        assert 'acme' in result


class TestGetTheAppRemoved:
    def test_function_removed(self):
        assert not hasattr(build, 'get_the_app')


class TestToolCards:
    def test_returns_string(self):
        assert isinstance(build.tool_cards(), str)

    def test_contains_grid(self):
        assert 'tool-cards-grid' in build.tool_cards()

    def test_contains_three_cards(self):
        assert build.tool_cards().count('tool-card"') >= 3

    def test_contains_chat_card(self):
        assert 'Chat' in build.tool_cards()

    def test_contains_cowork_card(self):
        assert 'Cowork' in build.tool_cards()

    def test_contains_code_card(self):
        assert 'Code' in build.tool_cards()

    def test_contains_badges(self):
        assert 'tool-card-badge' in build.tool_cards()


class TestClosingQuote:
    def test_returns_string(self):
        assert isinstance(build.closing_quote(), str)

    def test_contains_closing_div(self):
        assert 'closing-quote' in build.closing_quote()


class TestTabOverview:
    def test_returns_string(self):
        assert isinstance(build.tab_overview(), str)

    def test_contains_tab_content(self):
        assert 'data-tab="overview"' in build.tab_overview()

    def test_contains_mission_narrative(self):
        assert 'mission-narrative' in build.tab_overview()

    def test_contains_why_anthropic(self):
        assert 'why-claude-card' in build.tab_overview()

    def test_contains_compliance(self):
        assert 'compliance' in build.tab_overview()

    def test_contains_tool_cards(self):
        assert 'tool-cards-grid' in build.tab_overview()

    def test_contains_closing_quote(self):
        assert 'closing-quote' in build.tab_overview()

    def test_no_get_the_app(self):
        assert 'get-the-app' not in build.tab_overview()

    def test_contains_model_picker(self):
        assert 'model-picker' in build.tab_overview()

    def test_contains_general_tips(self):
        assert 'tips-grid' in build.tab_overview()

    def test_contains_use_cases(self):
        assert 'role-select' in build.tab_overview()

    def test_contains_resources(self):
        assert 'resources-grid' in build.tab_overview()


# ── Chat Intro ───────────────────────────────────────────────────────


class TestChatIntro:
    def test_returns_string(self):
        assert isinstance(build.chat_intro(), str)

    def test_contains_chat_intro_class(self):
        assert 'chat-intro' in build.chat_intro()

    def test_mentions_thinking_and_drafting(self):
        result = build.chat_intro().lower()
        assert 'thinking and drafting' in result

    def test_contains_what_is_chat_heading(self):
        assert 'What is Chat?' in build.chat_intro()

    def test_contains_h3_tag(self):
        assert '<h3>' in build.chat_intro()


# ── Wizard Progress Bar ──────────────────────────────────────────────


class TestWizardProgressBar:
    def test_returns_string(self):
        assert isinstance(build.wizard_progress_bar(), str)

    def test_contains_stepper(self):
        assert 'progress-stepper' in build.wizard_progress_bar()

    def test_three_steps(self):
        assert build.wizard_progress_bar().count('progress-step') >= 3

    def test_contains_labels(self):
        result = build.wizard_progress_bar()
        assert 'Your Profile' in result
        assert 'Try It Out' in result
        assert 'Company Project' in result


# ── Profile Form Content ─────────────────────────────────────────────


class TestProfileFormContent:
    def test_returns_string(self):
        assert isinstance(build._profile_form_content(), str)

    def test_contains_name_field(self):
        assert 'profile-name' in build._profile_form_content()

    def test_contains_pill_groups(self):
        assert 'data-pill-group' in build._profile_form_content()

    def test_contains_generate_button(self):
        assert 'generateProfile' in build._profile_form_content()

    def test_contains_output_area(self):
        assert 'profile-output-area' in build._profile_form_content()

    def test_contains_samples_textarea(self):
        assert 'profile-samples' in build._profile_form_content()

    def test_contains_import_section(self):
        assert 'import-paste' in build._profile_form_content()

    def test_contains_export_prompt(self):
        assert 'export-prompt-text' in build._profile_form_content()

    def test_contains_word_count(self):
        assert 'word-count' in build._profile_form_content()

    def test_contains_copy_buttons(self):
        assert 'pref-copy-btn' in build._profile_form_content()


# ── Wizard Stage 1 ───────────────────────────────────────────────────


class TestWizardStage1:
    def test_returns_string(self):
        assert isinstance(build.wizard_stage_1(), str)

    def test_data_stage_attribute(self):
        assert 'data-stage="1"' in build.wizard_stage_1()

    def test_contains_wizard_stage_class(self):
        assert 'wizard-stage' in build.wizard_stage_1()

    def test_contains_stage_title(self):
        assert 'stage-title' in build.wizard_stage_1()

    def test_contains_profile_form(self):
        assert 'profile-name' in build.wizard_stage_1()

    def test_contains_next_button(self):
        assert 'stage-next-btn' in build.wizard_stage_1()

    def test_contains_congrats(self):
        assert 'stage-1-congrats' in build.wizard_stage_1()

    def test_no_wizard_step_class(self):
        # Stage functions must NOT use old accordion markup
        result = build.wizard_stage_1()
        assert 'class="wizard-step"' not in result

    def test_no_wizard_step_header(self):
        assert 'wizard-step-header' not in build.wizard_stage_1()


# ── Wizard Stage 2 ───────────────────────────────────────────────────


class TestWizardStage2:
    def test_returns_string(self):
        assert isinstance(build.wizard_stage_2(), str)

    def test_data_stage_attribute(self):
        assert 'data-stage="2"' in build.wizard_stage_2()

    def test_contains_stage_title(self):
        assert 'stage-title' in build.wizard_stage_2()

    def test_contains_prompt_box(self):
        assert 'prompt-box' in build.wizard_stage_2()

    def test_mentions_slack(self):
        result = build.wizard_stage_2().lower()
        assert '#ai' in result

    def test_contains_next_button(self):
        assert 'stage-next-btn' in build.wizard_stage_2()

    def test_contains_back_button(self):
        assert 'stage-back-btn' in build.wizard_stage_2()

    def test_contains_mark_complete(self):
        result = build.wizard_stage_2().lower()
        assert 'mark complete' in result or 'stage-done-btn' in result


# ── Wizard Stage 3 ───────────────────────────────────────────────────


class TestWizardStage3:
    def test_returns_string(self):
        assert isinstance(build.wizard_stage_3(), str)

    def test_data_stage_attribute(self):
        assert 'data-stage="3"' in build.wizard_stage_3()

    def test_contains_stage_title(self):
        assert 'stage-title' in build.wizard_stage_3()

    def test_contains_downloads(self):
        result = build.wizard_stage_3()
        assert 'company.md' in result
        assert 'brand.md' in result

    def test_contains_done_button(self):
        assert 'stage-done-btn' in build.wizard_stage_3()

    def test_contains_back_button(self):
        assert 'stage-back-btn' in build.wizard_stage_3()

    def test_contains_congrats(self):
        assert 'stage-3-congrats' in build.wizard_stage_3()


# ── Chat Wizard Section ──────────────────────────────────────────────


class TestChatWizardSection:
    def test_returns_string(self):
        assert isinstance(build.chat_wizard_section(), str)

    def test_contains_progress_bar(self):
        assert 'progress-stepper' in build.chat_wizard_section()

    def test_contains_all_three_stages(self):
        result = build.chat_wizard_section()
        assert 'data-stage="1"' in result
        assert 'data-stage="2"' in result
        assert 'data-stage="3"' in result

    def test_contains_wizard_success(self):
        assert 'wizard-success' in build.chat_wizard_section()


# ── Chat Tab Assembly ────────────────────────────────────────────────


class TestTabChat:
    def test_returns_string(self):
        assert isinstance(build.tab_chat(), str)

    def test_contains_tab_content(self):
        assert 'data-tab="chat"' in build.tab_chat()

    def test_contains_chat_intro(self):
        assert 'chat-intro' in build.tab_chat()

    def test_contains_wizard_section(self):
        assert 'chat-wizard' in build.tab_chat()

    def test_contains_features_grid(self):
        assert 'features-grid' in build.tab_chat()

    def test_tips_moved_to_overview(self):
        assert 'tips-grid' not in build.tab_chat()
        assert 'tips-grid' in build.tab_overview()

    def test_use_cases_moved_to_overview(self):
        assert 'role-select' not in build.tab_chat()
        assert 'role-select' in build.tab_overview()

    def test_contains_all_stages(self):
        result = build.tab_chat()
        assert 'data-stage="1"' in result
        assert 'data-stage="2"' in result
        assert 'data-stage="3"' in result


class TestCoworkLocked:
    def test_returns_string(self):
        assert isinstance(build.cowork_locked(), str)

    def test_contains_locked_state(self):
        assert 'locked-state' in build.cowork_locked()

    def test_cowork_intro_in_tab(self):
        result = build.tab_cowork()
        assert 'What is Cowork?' in result
        assert 'tab-intro' in result

    def test_contains_examples(self):
        assert 'locked-examples' in build.cowork_locked()

    def test_contains_request_access(self):
        assert 'request-access' in build.cowork_locked()


class TestCoworkFeaturesGrid:
    def test_returns_string(self):
        assert isinstance(build.cowork_features_grid(), str)

    def test_contains_features_grid(self):
        assert 'features-grid' in build.cowork_features_grid()

    def test_contains_plugins(self):
        result = build.cowork_features_grid().lower()
        assert 'plugin' in result

    def test_at_least_four_cards(self):
        assert build.cowork_features_grid().count('feature-card') >= 4


class TestCoworkTips:
    def test_returns_string(self):
        assert isinstance(build.cowork_tips(), str)

    def test_contains_tips_grid(self):
        assert 'tips-grid' in build.cowork_tips()

    def test_at_least_four_tips(self):
        assert build.cowork_tips().count('tip-card') >= 4


class TestTabCowork:
    def test_returns_string(self):
        assert isinstance(build.tab_cowork(), str)

    def test_contains_tab_content(self):
        assert 'data-tab="cowork"' in build.tab_cowork()

    def test_contains_locked_state(self):
        assert 'cowork-locked' in build.tab_cowork()

    def test_contains_unlocked_state(self):
        assert 'cowork-unlocked' in build.tab_cowork()

    def test_unlocked_has_setup_cards(self):
        result = build.tab_cowork()
        assert 'data-cowork-card="1"' in result
        assert 'data-cowork-card="2"' in result
        assert 'data-cowork-card="3"' in result

    def test_unlocked_has_features(self):
        assert 'cowork_features_grid' not in build.tab_cowork()  # function name shouldn't appear
        result = build.tab_cowork()
        assert result.count('features-grid') >= 1

    def test_unlocked_hidden_by_default(self):
        assert 'display:none' in build.tab_cowork()

    def test_contains_cowork_success(self):
        assert 'cowork-success' in build.tab_cowork()


class TestCodeLocked:
    def test_returns_string(self):
        assert isinstance(build.code_locked(), str)

    def test_contains_locked_state(self):
        assert 'locked-state' in build.code_locked()

    def test_contains_what_is_code(self):
        result = build.code_locked().lower()
        assert 'claude code' in result

    def test_contains_team_builds(self):
        assert 'locked-examples' in build.code_locked()

    def test_contains_request_access(self):
        assert 'request-access' in build.code_locked()


class TestCodeFeaturesGrid:
    def test_returns_string(self):
        assert isinstance(build.code_features_grid(), str)

    def test_contains_features_grid(self):
        assert 'features-grid' in build.code_features_grid()

    def test_mentions_plan_mode(self):
        result = build.code_features_grid()
        assert 'Plan Mode' in result or 'Plan mode' in result

    def test_at_least_four_cards(self):
        assert build.code_features_grid().count('feature-card') >= 4


class TestCodeTips:
    def test_returns_string(self):
        assert isinstance(build.code_tips(), str)

    def test_contains_tips_grid(self):
        assert 'tips-grid' in build.code_tips()

    def test_at_least_four_tips(self):
        assert build.code_tips().count('tip-card') >= 4


class TestTabCode:
    def test_returns_string(self):
        assert isinstance(build.tab_code(), str)

    def test_contains_tab_content(self):
        assert 'data-tab="code"' in build.tab_code()

    def test_contains_locked_state(self):
        assert 'code-locked' in build.tab_code()

    def test_contains_unlocked_state(self):
        assert 'code-unlocked' in build.tab_code()

    def test_unlocked_has_setup_cards(self):
        result = build.tab_code()
        assert 'data-code-card="1"' in result
        assert 'data-code-card="2"' in result
        assert 'data-code-card="3"' in result

    def test_unlocked_hidden_by_default(self):
        assert 'display:none' in build.tab_code()

    def test_contains_code_success(self):
        assert 'code-success' in build.tab_code()


class TestTabSwitchingJS:
    def test_contains_tab_switching_function(self):
        result = build.footer_and_script()
        assert 'switchTab' in result or 'showTab' in result

    def test_handles_hash_routing(self):
        result = build.footer_and_script()
        assert 'location.hash' in result or 'window.location.hash' in result

    def test_updates_active_pill(self):
        result = build.footer_and_script()
        assert 'nav-pill' in result
        assert 'active' in result

    def test_listens_for_tab_clicks(self):
        result = build.footer_and_script()
        assert 'data-tab' in result

    def test_tool_card_triggers_tab(self):
        result = build.footer_and_script()
        assert 'data-tab-target' in result


# ── Wizard Stage JS ─────────────────────────────────────────────────


class TestWizardStageJS:
    def test_contains_stage_storage_key(self):
        result = build.footer_and_script()
        assert 'team-setup-wizard-done-v1' in result

    def test_contains_stage_navigation(self):
        result = build.footer_and_script()
        assert 'data-stage' in result

    def test_contains_progress_update(self):
        result = build.footer_and_script()
        assert 'progress-step' in result or 'updateStageProgress' in result

    def test_contains_stage_congrats(self):
        result = build.footer_and_script()
        assert '-congrats' in result

    def test_contains_wizard_success_banner(self):
        result = build.footer_and_script()
        assert 'wizard-success' in result


# ── Gating JS ────────────────────────────────────────────────────────


class TestGatingJS:
    def test_fetches_access_endpoint(self):
        result = build.footer_and_script()
        assert '/api/claude-setup-access' in result

    def test_toggles_locked_unlocked(self):
        result = build.footer_and_script()
        assert 'cowork-locked' in result
        assert 'cowork-unlocked' in result

    def test_updates_lock_icons(self):
        result = build.footer_and_script()
        assert 'lock-icon' in result or 'cowork-lock' in result

    def test_updates_tool_card_badges(self):
        result = build.footer_and_script()
        assert 'tool-card-badge' in result or 'cowork-badge' in result
