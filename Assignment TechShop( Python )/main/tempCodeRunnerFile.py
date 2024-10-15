product_id)
                        if product: 
                            dao.add_order_detail(customer_id,product_id, quantity)  
                        else:
                            print("Product not found.")

                    dao.add_order(order)

                elif order_choice == "2":
                    # Update Order Status
                    order_id = int(input("Enter order ID: "))
                    status = input("Enter new status (e.g., Processing, Shipped): ")
                    dao.update_order_status(order_id, status)

                elif order_choice == "3":
                    # Remove Order
                    order_id = int(input("Enter order ID to remove: "))
                    dao.delete_order(order_id)

                elif order_choice == "4":
                    # List All Orders
                    orders = dao.li