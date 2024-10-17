createRoutesFromElements(
    <Route path="/" element={<Root />}> 
        <Route errorElement={<ErrorPage />}>
            <Route index element={<Index/>} />
        <var>
            <Route path="contacts/:contactId"element={<Contact />} />
            <Route path="contacts/:contactId/edit"element={<EditContact />} />
            <Route path="contacts/:contactId/destroy" />
        </Route>
    </Route>
        </var>
            


)