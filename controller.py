import model
import text_fields as txt
import view


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_success)
            case 2:
                model.save_file()
                view.print_info(txt.save_success)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_success)
            case 5:
                lookup_contact = view.search_name(choice)
                view.show_contacts(model.search_contact(lookup_contact), txt.contact_not_found)
            case 6:
                contact_index = view.search_name(choice) - 1
                parameter_to_change = view.ask_change_parameter()
                new_value = view.get_new_value()
                model.edit_contact(contact_index, parameter_to_change, new_value)
                view.print_info(txt.change_success)

            case 7:
                lookup_contact = view.search_name(choice)
                view.deletion_success(model.delete_contact(lookup_contact))
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                view.print_info(txt.bye_bye)
                exit()
